@echo off
cd /d %~dp0
if not exist .venv\Scripts\python.exe (
  echo Create the environment first: python -m venv .venv
  pause
  exit /b 1
)
.venv\Scripts\python.exe -m uvicorn backend.main:app --reload --port 8000
