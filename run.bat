@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  python -m venv .venv
  .venv\Scripts\pip.exe install -r app\requirements.txt
)
.venv\Scripts\python.exe app\app.py
