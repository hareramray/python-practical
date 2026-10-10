@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\jupyter-lab.exe" (
  echo Please follow the setup instructions in README.md first.
  pause
  exit /b 1
)
".venv\Scripts\jupyter-lab.exe" notebooks\00_start_here.ipynb
