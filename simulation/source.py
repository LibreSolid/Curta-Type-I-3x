"""Make repeated STEP product names unambiguous without changing geometry.

The export reuses names for distinct products (including subassemblies). The
public StepNode selects by name, so an ignored import copy gives each repeated
name its existing STEP entity number. Every other byte remains upstream's.
"""

from collections import Counter
from pathlib import Path
import re


SOURCE = Path(__file__).resolve().parents[1] / "CAD" / "Curta Assembly.step"
STEP = Path(__file__).resolve().parent / "_source" / "curta.step"
PRODUCT = re.compile(r"(#\d+=PRODUCT\('(?:''|[^'])*',\s*')((?:''|[^'])*)(')")


def unique_names(text):
    """Return the name-only import copy and its entity-to-name mapping."""
    counts = Counter(match[2] for match in PRODUCT.finditer(text))
    renamed = {}

    def rename(match):
        prefix, name, suffix = match.groups()
        if counts[name] > 1:
            entity = prefix.split("=", 1)[0]
            renamed[entity] = name
            name = f"{name} [{entity}]"
        return prefix + name + suffix

    return PRODUCT.sub(rename, text), renamed


def prepare():
    """Materialize the deterministic import copy; preserve mtime when current."""
    content, renamed = unique_names(SOURCE.read_text())
    if not STEP.exists() or STEP.read_text() != content:
        STEP.parent.mkdir(parents=True, exist_ok=True)
        STEP.write_text(content)
    return renamed


if __name__ == "__main__":
    for entity, name in prepare().items():
        print(f"{entity}: {name}")
