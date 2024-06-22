#pip install pyinstaller

REM Check if a file was dragged and dropped
if "%~1"=="" (
    echo Please drag and drop a .py file onto this .bat file to package it into an executable.
    pause
    exit /b 1
)
REM Set the path for PyInstaller output
set "DIST_DIR=%~dp0Output"
set "WORK_DIR=%DIST_DIR%\build"
set "SPEC_DIR=%DIST_DIR%"

REM Ensure the output directories exist
mkdir "%DIST_DIR%"
mkdir "%WORK_DIR%"

#run below code to build python to exe
REM Run PyInstaller with the specified paths
python -m PyInstaller --onefile --distpath "%DIST_DIR%" --workpath "%WORK_DIR%" --specpath "%SPEC_DIR%" "%~1"

pause