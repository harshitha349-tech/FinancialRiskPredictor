@echo off
setlocal
cd /d %~dp0
echo ==========================================
echo       CreditLens - First-time setup
echo ==========================================
where python >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install Python 3.10-3.12 and enable Add to PATH.
  pause
  exit /b 1
)
if not exist .venv\Scripts\python.exe (
  python -m venv .venv
  if errorlevel 1 goto failed
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 goto failed
cd frontend
where npm >nul 2>nul
if errorlevel 1 (
  echo npm was not found. Install the current Node.js LTS release, then rerun setup.
  pause
  exit /b 1
)
npm install
if errorlevel 1 goto failed
cd ..
echo.
echo Setup completed. Double-click start_demo.bat to run CreditLens.
pause
exit /b 0
:failed
echo.
echo Setup failed. Check the error above, your internet connection, and installed Python/Node versions.
pause
exit /b 1
