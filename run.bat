@echo off
setlocal enableextensions
cd /d "%~dp0"
title FluffBrowser

rem Keep Cyrillic and box-drawing characters intact in every console.
chcp 65001 >nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"

echo.
echo   FluffBrowser
echo   ============
echo.

if exist ".venv\Scripts\python.exe" goto :ready

rem -- Find an interpreter: py launcher, PATH, then the usual install folders --
set "PYTHON="
where py >nul 2>nul && set "PYTHON=py -3"
if not defined PYTHON (
    where python >nul 2>nul && set "PYTHON=python"
)
if not defined PYTHON for %%V in (313 312 311) do (
    if not defined PYTHON if exist "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" (
        set PYTHON="%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe"
    )
)
if not defined PYTHON for %%V in (313 312 311) do (
    if not defined PYTHON if exist "%ProgramFiles%\Python%%V\python.exe" (
        set PYTHON="%ProgramFiles%\Python%%V\python.exe"
    )
)

if not defined PYTHON (
    echo   Python 3.11+ was not found.
    echo   Install it from https://www.python.org/downloads/
    echo   and tick "Add python.exe to PATH", then run this file again.
    echo.
    pause
    exit /b 1
)

echo   [1/3] Creating virtual environment (.venv)...
%PYTHON% -m venv .venv
if not exist ".venv\Scripts\python.exe" (
    echo.
    echo   Could not create a virtual environment with: %PYTHON%
    echo   Install Python 3.11+ from https://www.python.org/downloads/
    echo   and run this file again.
    echo.
    pause
    exit /b 1
)

echo   [2/3] Installing dependencies (first launch only)...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo   Dependency installation failed. Check your connection and retry.
    echo.
    pause
    exit /b 1
)

:ready
if /i "%~1"=="--update" ".venv\Scripts\python.exe" -m pip install --upgrade -r requirements.txt

if not exist ".venv\.chromium-ok" (
    echo   [3/3] Downloading Chromium -- first launch only...
    ".venv\Scripts\python.exe" -m playwright install chromium
    if errorlevel 1 (
        echo.
        echo   Chromium download failed. Retry with:
        echo     .venv\Scripts\python.exe -m playwright install chromium
        echo.
    ) else (
        echo installed > ".venv\.chromium-ok"
    )
)

echo   Launching FluffBrowser...
echo.
".venv\Scripts\python.exe" startbrowser.py
if errorlevel 1 (
    echo.
    echo   FluffBrowser exited with an error. Read the message above.
)

echo.
pause
endlocal
