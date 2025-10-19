"""Execute the B2 notebook with pure Python to verify it runs without external dependencies."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def execute_notebook(path: Path) -> None:
    nb = json.loads(path.read_text())
    namespace: dict[str, object] = {"__name__": "__main__"}
    for index, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if not source.strip():
            continue
        try:
            compiled = compile(source, f"notebook_cell_{index}", "exec")
            exec(compiled, namespace)
        except Exception as exc:  # pragma: no cover - troubleshooting helper
            raise RuntimeError(f"Error while executing cell {index}: {exc}") from exc


DEFAULT_NOTEBOOK = Path(__file__).parents[1] / "B2" / "b2_first_steps.ipynb"


def main(args: list[str]) -> int:
    target = Path(args[0]) if args else DEFAULT_NOTEBOOK
    execute_notebook(target)
    print("Notebook executed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
