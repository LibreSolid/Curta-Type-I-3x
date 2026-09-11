"""A label adaptation must never rewrite geometry or conflate products."""

from collections import Counter
import re
import unittest

from simulation.source import PRODUCT, SOURCE, unique_names


class SourceTest(unittest.TestCase):
    def test_only_duplicate_product_names_change(self):
        original = SOURCE.read_text()
        prepared, renamed = unique_names(original)
        restored = prepared
        for entity, name in renamed.items():
            restored = restored.replace(f"'{name} [{entity}]'", f"'{name}'")
        self.assertEqual(restored, original)
        names = Counter(match[2] for match in PRODUCT.finditer(prepared))
        self.assertEqual(len(names), 276)
        self.assertEqual(set(names.values()), {1})
        self.assertEqual(sum(name == "M4x10" for name in renamed.values()), 2)
        self.assertEqual(sum(name == "6mm ball" for name in renamed.values()), 2)

    def test_unique_source_products_keep_their_names(self):
        prepared, _ = unique_names(SOURCE.read_text())
        self.assertIn("'main body','main body','main body'", prepared)
        self.assertEqual(len(re.findall(r"=PRODUCT\(", prepared)), 276)


if __name__ == "__main__":
    unittest.main()
