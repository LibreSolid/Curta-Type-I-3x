"""Mechanically compact the one-shot STEP scaffold, preserving its operations.

Run immediately after `solid import-step ... --into simulation/standard`.
This removes repetitive generated comments and empty render methods, and shares
the STEP path/tessellation on one base class. It does not infer any mechanics.
"""

import ast
from pathlib import Path


def compact(directory):
    for filename in ("parts.py", "assembly.py"):
        path = directory / filename
        lines = path.read_text().splitlines()
        lines = [line for line in lines if not line.lstrip().startswith("#")]
        # The CLI emits comment-only render bodies for identity placements.
        for index in range(len(lines) - 1, -1, -1):
            if lines[index].strip() == "def render(self):":
                following = next((line for line in lines[index + 1:] if line.strip()), "")
                if not following.startswith("        "):
                    lines.pop(index)
        tree = ast.parse("\n".join(lines))
        if filename == "parts.py":
            for item in tree.body:
                if isinstance(item, ast.ClassDef):
                    item.bases = [ast.Name(id="SourcePart", ctx=ast.Load())]
                    item.body = [statement for statement in item.body
                                 if not (isinstance(statement, ast.Assign)
                                         and statement.targets[0].id in
                                         {"step_source", "angular_deflection"})]
            tree.body[1:2] = ast.parse('''
from solid_node.node import StepNode
from simulation.source import STEP, prepare

prepare()

class SourcePart(StepNode):
    step_source = str(STEP)
    angular_deflection = 0.5
''').body
        ast.fix_missing_locations(tree)
        path.write_text(ast.unparse(tree) + "\n")


if __name__ == "__main__":
    compact(Path(__file__).resolve().parents[1] / "standard")
