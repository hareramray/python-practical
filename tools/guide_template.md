# Learn Python by doing

A practical course with **24 learning notebooks, 48 exercises with checks, 24 worked-solution notebooks, and a mini-project prompt in each lesson**. Start from zero and progress into advanced Python and expert engineering practices. The final notebook builds a working expense pipeline with validation, SQLite storage, reporting, and export.

This course develops the foundations for expert work; expertise also takes sustained practice on larger projects, reading other people's code, and feedback. You do not need prior programming experience for notebook 00.

## Start on this computer

Double-click **`start_learning.cmd`** in this folder. It opens JupyterLab with [00_start_here.ipynb](notebooks/00_start_here.ipynb). Leave the terminal running while you learn. To stop, return to the terminal, press Ctrl+C, and follow any shutdown prompt.

Or run this in PowerShell from the project folder:

```powershell
.\.venv\Scripts\jupyter-lab.exe notebooks\00_start_here.ipynb
```

The local `.venv` contains Python's notebook tools, NumPy, pandas, and matplotlib. You do not need to activate the environment or change PowerShell's execution policy when using these commands. In VS Code, open a notebook, choose **Select Kernel → Python Environments**, and choose this project's `.venv`. The Python and Jupyter extensions are needed for that workflow.

If JupyterLab shows a URL rather than opening a browser, open the displayed local URL. Keep its access token private. If a package import fails, inspect `sys.executable` in notebook 00 and select the project interpreter.

## Setup on another computer, or recreate the environment

The course was built for Python 3.13; use 3.13 or newer. These are **terminal commands**, not notebook code. Choose either route below.

With an installed Python interpreter on Windows:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name python3 --display-name "Python 3 (ipykernel)"
.\.venv\Scripts\jupyter-lab.exe notebooks\00_start_here.ipynb
```

Or with `uv`:

```powershell
uv venv --python 3.13 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name python3 --display-name "Python 3 (ipykernel)"
.\.venv\Scripts\jupyter-lab.exe notebooks\00_start_here.ipynb
```

On macOS/Linux, create the environment with `python3 -m venv .venv`, then use `.venv/bin/python` and `.venv/bin/jupyter-lab` in place of the Windows executable paths. Do not copy `.venv` between computers; recreate it. `requirements.txt` lists the direct dependencies with version ranges. `requirements-tested.txt` records the exact tested Windows environment; it includes platform-specific packages and is primarily a reproduction record for Windows.

Package installation needs internet access. The lessons themselves use embedded sample data and require no accounts, API keys, or external services. Notebook 17 opens a short-lived HTTP server on loopback (`127.0.0.1`) to demonstrate real HTTP locally. Examples use temporary folders or in-memory databases, so they do not overwrite personal files.

## How to learn from each notebook

1. Read a short explanation and **predict** the code's output.
2. Run the example with **Shift+Enter** and compare it with your prediction.
3. Do the **Try a change** experiment. Explain why the result changed.
4. Fill in each exercise's starter cell. Then change its `exercise_1_ready` or `exercise_2_ready` flag to `True` and run the check cell. Read a failed assertion as feedback.
5. Try the mini-project in the provided workspace. These open-ended projects do not have complete supplied answers, except for the demonstrated capstone workflow.
6. Use **Restart Kernel and Run All** to check that your work does not rely on hidden state. Record progress in [PROGRESS.md](PROGRESS.md).

Exercise checks are deliberately disabled at first so unfinished starter notebooks still run. **A clean Run All does not mean your exercises are solved unless their checks are enabled.** The separate solution notebooks contain complete exercise implementations with checks enabled. Compare them only after making a serious attempt; other implementations can also be correct.

Work in numerical order. Each notebook is independent of other notebooks' variables and generated files, but assumes you understand earlier concepts. Run cells within a notebook from top to bottom. If you change an example's data, an assertion based on its original data may need to change too.

## Course map

| # | Learning notebook | Stage | Worked exercises |
|---|---|---|---|
<!-- COURSE_TABLE -->

## Suggested pace and checkpoints

Spend 30–60 minutes per session, three to five times per week. A notebook may take more than one session, especially once projects become larger. Move forward when you can explain and change the code, not just rerun it.

- **Foundation — 00–05:** build a bill splitter and text-based grade report without copying. Explain types, collection choices, loops, and return values.
- **Reliable programs — 06–10:** build a file-backed task tracker with validation and tests. Reproduce and fix a bug using a small failing case.
- **Advanced language — 11–15:** build a lazy processing pipeline and explain its memory tradeoffs. Use classes, generators, decorators, and types where they simplify the design.
- **Connected programs — 16–18:** query a database safely, handle a local HTTP response, and demonstrate bounded concurrent I/O.
- **Data practice — 19–21:** clean a dataset, reconcile totals, and produce a labeled chart with an honest written interpretation.
- **Engineering and capstone — 22–23:** measure a real bottleneck, separate calculations from I/O, and complete the expense pipeline extensions with failure-path tests.

Return to earlier notebooks after a few days and recreate one exercise in a blank cell. If you get stuck, use a hint, reduce the input to a tiny example, and inspect intermediate values before opening the answer notebook.

## Files and validation

- `notebooks/`: the lessons you edit and practice in.
- `solutions/`: matching notebooks with worked exercise implementations and enabled checks.
- `PROGRESS.md`: your editable completion tracker.
- `start_learning.cmd`: launches the local JupyterLab environment on Windows.
- `tools/validate_course.py`: validates notebook structure and executes each notebook in its own fresh kernel. By default, executed copies go to `.validation/` so your notebooks are not overwritten.
- `tools/build_course.py`: authoring source, **not needed for learning**. It refuses to replace existing notebooks unless `--overwrite` is supplied. Regeneration replaces notebook edits, README, and the progress tracker; back up your work before doing that.

To validate the course from PowerShell:

```powershell
.\.venv\Scripts\python.exe tools\validate_course.py
```

Use `--write-outputs` only when you want to refresh saved outputs in the source notebooks. Validation runs your notebook code; it also respects any exercise flags you have enabled. The generated `validation_report.json` records completion and code-cell counts.

## Further reading

Use these when you want more detail after trying a lesson:

- [Official Python tutorial](https://docs.python.org/3.13/tutorial/) — language features and standard-library introductions; it assumes some programming familiarity.
- [Python standard-library reference](https://docs.python.org/3.13/library/) — details for modules used in this course.
- [Official Jupyter installation guide](https://jupyter.org/install) — JupyterLab and notebook installation.
- [NumPy learning resources](https://numpy.org/learn/) — numerical arrays and scientific computing.
- [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html) — tables and data analysis.
- [matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html) — plotting techniques.

Choose a specialization after the capstone: automation, backend development, data analysis, scientific computing, or machine learning. Build a project you actually want to use, and keep adding tests and reviewing the design as it grows.
