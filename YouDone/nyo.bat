@echo off
title Locked Batch File

:check_running
tasklist | find /i "cmd.exe" | find /i "helper.bat" > nul
if errorlevel 1 (
    echo Batch file is not running. Restarting...
    start /min cmd /c "helper.bat"
)
timeout /t 5 > nul
goto check_running