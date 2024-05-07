@REM setlocal enabledelayedexpansion

set "mp3_found=false"
set "mp4_found=false"
set "mp3_files="
set "mp4_files="

for %%i in (*.mp3 *.mp4) do (
    if "%%~xi"==".mp3" (
        set mp3_found=true
        set "mp3_files=!mp3_files!%%i|"
    )
    if "%%~xi"==".mp4" (
        set mp4_found=true
        set "mp4_files=!mp4_files!%%i|"
    )
)

if "%mp3_found%"=="true" (
    echo MP3-Datei gefunden!
)

if "%mp4_found%"=="true" (
    echo MP4-Datei gefunden!
)

if "%mp3_files%" NEQ "" (
    echo Gefundene MP3-Dateien: %mp3_files:~0,-1%
)

if "%mp4_files%" NEQ "" (
    echo Gefundene MP4-Dateien: %mp4_files:~0,-1%
)

pause
