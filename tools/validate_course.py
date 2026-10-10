"""Execute each notebook in an isolated kernel and verify the course artifacts."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import time

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]


def check_notebook(path: Path, write_outputs: bool) -> dict:
    started = time.perf_counter()
    relative = path.relative_to(ROOT)
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    client = NotebookClient(notebook, timeout=120, kernel_name="python3",
                            resources={"metadata": {"path": str(path.parent)}},
                            record_timing=False)
    client.execute()
    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    assert all(cell.execution_count is not None for cell in code_cells), "Unexecuted code cell"
    assert not any(output.output_type == "error" for cell in code_cells for output in cell.outputs), "Error output"
    # Guard against accidentally disabled solution checks.
    checks = [cell for cell in code_cells if "exercise-check" in cell.metadata.get("tags", [])]
    assert len(checks) == 2, "Each notebook must contain two exercise checks"
    if path.parent.name == "solutions":
        for cell in checks:
            output = "".join(item.get("text", "") for item in cell.outputs if item.output_type == "stream")
            assert "supplied checks passed" in output, "Solution exercise check did not run"
    destination = path if write_outputs else ROOT / ".validation" / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, destination)
    return {"notebook": relative.as_posix(), "status": "passed", "code_cells": len(code_cells),
            "seconds": round(time.perf_counter() - started, 2)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-outputs", action="store_true")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    learners = sorted((ROOT / "notebooks").glob("*.ipynb"))
    solutions = sorted((ROOT / "solutions").glob("*.ipynb"))
    assert len(learners) == len(solutions) == 24, "Expected 24 lessons and 24 solution notebooks"
    assert {p.stem + "_solutions" for p in learners} == {p.stem for p in solutions}
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        pending = {executor.submit(check_notebook, path, args.write_outputs): path for path in learners + solutions}
        for future in as_completed(pending):
            path = pending[future]
            try:
                result = future.result()
            except Exception as error:
                result = {"notebook": path.relative_to(ROOT).as_posix(), "status": "failed", "error": str(error)}
            results.append(result)
            print(f"{result['status'].upper()}: {result['notebook']}", flush=True)
            if result["status"] == "failed":
                print(result["error"], flush=True)
    report = {"notebooks": sorted(results, key=lambda row: row["notebook"]),
              "passed": sum(row["status"] == "passed" for row in results),
              "failed": sum(row["status"] == "failed" for row in results),
              "code_cells_executed": sum(row.get("code_cells", 0) for row in results)}
    (ROOT / "validation_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Validated {report['passed']}/{len(results)} notebooks; {report['code_cells_executed']} code cells executed.")
    raise SystemExit(1 if report["failed"] else 0)


if __name__ == "__main__":
    main()
