"""Regression checks for publication boundaries and preservation of user notes."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


checker = module('validate_public')
initializer = module('init_workspace')


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=os.environ.get('GAMING_OS_TEST_TMP'))
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'framework'
        manifest = json.loads((ROOT / 'PUBLIC-FILES.json').read_text(encoding='utf-8'))
        for name in [row['path'] for row in manifest['files']] + ['PUBLIC-FILES.json']:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def test_clean_distribution(self):
        self.assertEqual(checker.validate(self.root)['status'], 'PASS')

    def test_game_file_rejected(self):
        target = self.root / 'games' / 'example' / 'design.md'
        target.parent.mkdir(parents=True)
        target.write_text('Unpublished user design', encoding='utf-8')
        self.assertEqual(checker.validate(self.root)['status'], 'FAIL')
        self.assertEqual(checker.validate(self.root, refresh=True)['status'], 'FAIL')

    def test_hash_drift_rejected(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as handle:
            handle.write('\nUnreviewed edit\n')
        self.assertEqual(checker.validate(self.root)['status'], 'FAIL')

    def test_credential_cannot_be_blessed_by_refresh(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as handle:
            handle.write('\n' + 'gh' + 'p_' + 'A' * 40 + '\n')
        self.assertEqual(checker.validate(self.root, refresh=True)['status'], 'FAIL')

    def test_personal_machine_path_rejected(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as handle:
            handle.write('\n' + 'C:' + chr(92) + 'Users' + chr(92) + 'example-user\n')
        self.assertEqual(checker.validate(self.root, refresh=True)['status'], 'FAIL')

    def test_manifest_cannot_add_a_game(self):
        path = self.root / 'PUBLIC-FILES.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['files'].append({'path': 'games/example/state.md', 'sha256': '', 'bytes': 0})
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(checker.validate(self.root, refresh=True)['status'], 'FAIL')

    def test_private_notes_not_overwritten(self):
        target = self.root / 'workspace'
        names = initializer.initialize(target, self.root)
        memory = target / 'MEMORY.md'
        memory.write_text('User decisions to preserve\n', encoding='utf-8')
        before = {name: (target / name).read_bytes() for name in names}
        with self.assertRaises(FileExistsError):
            initializer.initialize(target, self.root)
        self.assertEqual(before, {name: (target / name).read_bytes() for name in names})
        self.assertEqual(checker.validate(self.root)['status'], 'PASS')


if __name__ == '__main__':
    unittest.main()
