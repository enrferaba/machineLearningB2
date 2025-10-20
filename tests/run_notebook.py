"""Execute the notebooks with pure Python to verify they run without external dependencies."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def execute_notebook(path: Path) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    namespace: dict[str, object] = {"__name__": "__main__"}
    for index, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if not source.strip():
            continue
        try:
            compiled = compile(source, f"{path.name}_cell_{index}", "exec")
            exec(compiled, namespace)
        except Exception as exc:  # pragma: no cover - troubleshooting helper
            raise RuntimeError(f"Error while executing {path.name} cell {index}: {exc}") from exc


DEFAULT_NOTEBOOKS = [
    Path(__file__).parents[1] / "Machine Learning 1" / "b2" / "b2_python.ipynb",
]


def main(args: list[str]) -> int:
    targets = [Path(arg) for arg in args] if args else DEFAULT_NOTEBOOKS
    for notebook in targets:
        execute_notebook(notebook)
        print(f"Executed {notebook.name} successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
