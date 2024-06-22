
REM Check if a file was dragged and dropped
if "%~1"=="" (
    echo Please drag and drop a DxDiag.txt file onto this .bat file to package it into an executable. Ctrl+R DxDiag
    pause
    exit /b 1
)

py PCSpec.py %~1

pause