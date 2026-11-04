"""Create private working notes from public templates; never overwrite existing notes."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def initialize(target, root=ROOT):
    target = Path(target)
    sources = {
        'MEMORY.md': root / 'gaming-os/templates/project-memory.md',
        'PROJECT-STATE.md': root / 'gaming-os/templates/game-project-state.md',
        'SESSION-CHECKPOINT.md': root / 'gaming-os/templates/session-checkpoint.md',
    }
    outputs = {name: source.read_text(encoding='utf-8') for name, source in sources.items()}
    outputs['WORKLOG.md'] = '# Log kerja workspace\n\nCatat hasil sesi, bukti, batas dan langkah seterusnya di sini.\n'
    if target.is_symlink():
        raise ValueError('Refusing a symbolic-link workspace')
    if any((target / name).exists() for name in outputs):
        raise FileExistsError('Existing working notes found; nothing overwritten')
    target.mkdir(parents=True, exist_ok=True)
    for name, text in outputs.items():
        with (target / name).open('x', encoding='utf-8') as handle:
            handle.write(text)
    return sorted(outputs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path', type=Path, default=ROOT / 'workspace')
    args = parser.parse_args()
    try:
        created = initialize(args.path)
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')
    print('Created private working notes: ' + ', '.join(created))
    print('Keep this workspace out of the public framework history.')


if __name__ == '__main__':
    main()
