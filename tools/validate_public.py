"""Validate a framework-only distribution without reading private workspaces."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'PUBLIC-FILES.json'
BLOCKED = {'games', 'Resources', 'research', '00-project-control', '.toolchain',
           '.codex', '.aws', '.firecrawl', 'MEMORY.md', 'plan.md'}
SENSITIVE = [
    re.compile(r'gh[pousr]_[A-Za-z0-9]{30,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{30,}'),
    re.compile(r'sk-(?:proj-)?[A-Za-z0-9_-]{30,}'),
    re.compile(r'-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----'),
    re.compile(r'[A-Za-z]:[/\\](?:Users|OneDrive)[/\\]', re.I),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root=ROOT, refresh=False):
    root = Path(root).resolve()
    errors = []
    counts = {'files': 0, 'local_links': 0, 'asset_examples': 0, 'map_examples': 0}
    try:
        manifest = json.loads((root / MANIFEST).read_text(encoding='utf-8'))
        rows = manifest['files']
        if manifest.get('schema') != 'gaming-os.public-files.v1' or not isinstance(rows, list):
            raise ValueError('Invalid public manifest schema')
        paths = [row['path'] for row in rows]
        if len(paths) != len(set(paths)):
            errors.append('Duplicate manifest path')
        for name in paths:
            p = PurePosixPath(name)
            if (p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name
                    or name != p.as_posix() or not p.parts):
                errors.append('Unsafe manifest path')
                continue
            if (p.parts[0].casefold() in {n.casefold() for n in BLOCKED | {'workspace', '.git'}}
                    or name == MANIFEST or (p.name.startswith('.env') and p.name != '.env.example')
                    or p.suffix.lower() in {'.pem', '.key'}):
                errors.append('Private or reserved path in manifest: ' + name)
        if errors:
            return {'status': 'FAIL', 'checks': counts, 'errors': errors}
        expected = set(paths) | {MANIFEST}
        required = {'README.md', 'LICENSE', 'AGENTS.md', 'CLAUDE.md', 'gaming-os/SKILL.md',
                    'gaming-os/workflows/router.md', 'gaming-os/workflows/modes.md'}
        if not required <= expected:
            errors.append('Required framework entry files absent from manifest')
        actual = set()
        for path in root.rglob('*'):
            rel = path.relative_to(root)
            if rel.parts[0] in {'.git', 'workspace'} or '__pycache__' in rel.parts:
                continue
            if path.is_symlink():
                errors.append('Symbolic link in public tree: ' + rel.as_posix())
            elif path.is_file():
                actual.add(rel.as_posix())
        for name in sorted(actual - expected):
            errors.append('File outside public allowlist: ' + name)
        for name in sorted(expected - actual):
            errors.append('Missing public file: ' + name)
        if (root / '.git').exists():
            git = subprocess.run(['git', '-C', str(root), 'ls-files', '-z'],
                                 capture_output=True, check=True)
            tracked = set(git.stdout.decode('utf-8').strip('\0').split('\0')) - {''}
            for name in sorted(tracked - expected):
                errors.append('Tracked file outside public allowlist: ' + name)
        for row in rows:
            path = root / row['path']
            if not path.is_file() or path.is_symlink():
                continue
            raw = path.read_bytes()
            if not refresh and (digest(path) != row.get('sha256') or len(raw) != row.get('bytes')):
                errors.append('Hash or byte count differs: ' + row['path'])
            try:
                text = raw.decode('utf-8')
            except UnicodeError:
                errors.append('Public distribution expects UTF-8 text: ' + row['path'])
                continue
            if any(pattern.search(text) for pattern in SENSITIVE):
                errors.append('Potential credential or personal machine path: ' + row['path'])
            if path.suffix == '.md':
                for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
                    target = target.strip('<>')
                    if '://' in target or target.startswith(('#', 'mailto:')):
                        continue
                    target = unquote(target.split('#')[0])
                    resolved = (path.parent / target).resolve()
                    counts['local_links'] += 1
                    if not resolved.is_relative_to(root) or not resolved.exists():
                        errors.append('Invalid local link: ' + row['path'] + ' -> ' + target)
            counts['files'] += 1
        modules = sorted((root / 'gaming-os/references').glob('*.md'))
        if [p.name[:2] for p in modules] != [f'{n:02}' for n in range(1, 15)]:
            errors.append('Expected framework modules 01 through 14')
        router = (root / 'gaming-os/workflows/router.md').read_text(encoding='utf-8')
        modes = (root / 'gaming-os/workflows/modes.md').read_text(encoding='utf-8')
        for mode in ['RESEARCH', 'IDEATE', 'PLAN', 'ART', 'ASSET', 'BUILD', 'PLAYTEST',
                     'DIAGNOSE', 'ITERATE', 'RELEASE', 'CONTINUE', 'EDUCATE']:
            if f'| {mode} |' not in router or f'## {mode}\n' not in modes:
                errors.append('Work mode not routed: ' + mode)
        skill = (root / 'gaming-os/SKILL.md').read_text(encoding='utf-8')
        frontmatter = re.match(r'^---\n(.*?)\n---\n', skill, re.S)
        if not frontmatter or 'name: gaming-os\n' not in frontmatter.group(1) + '\n' or 'description:' not in frontmatter.group(1):
            errors.append('Invalid framework skill entry')
        counts['modules'] = len(modules)
        counts['modes'] = 12
        assets = json.loads((root / 'gaming-os/templates/asset-manifest.example.json').read_text(encoding='utf-8'))
        if not assets.get('example_only') or assets.get('schema') != 'gaming-os.asset-manifest.v1':
            errors.append('Invalid illustrative asset contract')
        for asset in assets['assets']:
            if asset['status'] != 'planned' or asset['review']['approved_by_owner']:
                errors.append('Example asset falsely claims generation or owner approval')
            width, height = asset['width'], asset['height']
            for frame in asset['frames']:
                x, y, w, h = frame['rect']
                if min(x, y) < 0 or min(w, h) <= 0 or x + w > width or y + h > height or frame['duration_ms'] <= 0:
                    errors.append('Invalid illustrative sprite frame')
            counts['asset_examples'] += 1
        level = json.loads((root / 'gaming-os/templates/map-contract.example.json').read_text(encoding='utf-8'))
        if (not level.get('example_only') or level.get('schema') != 'gaming-os.map-contract.v1'
                or level.get('reachability_status') != 'not_run'):
            errors.append('Invalid illustrative map contract')
        width, height = level['world']['width'], level['world']['height']
        for x, y in level['critical_points']:
            if not (0 <= x <= width and 0 <= y <= height):
                errors.append('Map critical point outside bounds')
            for block in level['collision']:
                bx, by, bw, bh = block['rect']
                if bx <= x < bx + bw and by <= y < by + bh:
                    errors.append('Map critical point inside collision')
        counts['map_examples'] = 1
        if refresh and not errors:
            for row in rows:
                path = root / row['path']
                row['sha256'] = digest(path)
                row['bytes'] = path.stat().st_size
            (root / MANIFEST).write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        errors.append('Validation could not complete: ' + str(error))
    return {'status': 'FAIL' if errors else 'PASS', 'checks': counts, 'errors': errors,
            'limitations': 'Framework structure, allowlist and basic privacy patterns only; not exhaustive disclosure review or game runtime evidence.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Refresh hashes only after a successful content/allowlist check')
    args = parser.parse_args()
    result = validate(refresh=args.refresh)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
