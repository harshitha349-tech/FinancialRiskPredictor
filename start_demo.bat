@echo off
cd /d %~dp0
if not exist .venv\Scripts\python.exe (
  echo Please run setup_windows.bat first.
  pause
  exit /b 1
)
if not exist frontend\node_modules (
  echo Frontend dependencies are missing. Please run setup_windows.bat first.
  pause
  exit /b 1
)
start "CreditLens Backend" cmd /k "cd /d ""%~dp0"" && .venv\Scripts\python.exe -m uvicorn backend.main:app --reload --port 8000"
start "CreditLens Frontend" cmd /k "cd /d ""%~dp0frontend"" && npm run dev"
timeout /t 3 /nobreak >nul
start "" http://localhost:5173
