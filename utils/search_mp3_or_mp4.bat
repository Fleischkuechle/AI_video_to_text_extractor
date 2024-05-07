@REM setlocal enabledelayedexpansion

set "mp3_found=false"
set "mp4_found=false"

for %%i in (*.mp3 *.mp4) do (
    if "%%~xi"==".mp3" set mp3_found=true
    if "%%~xi"==".mp4" set mp4_found=true
)

if "%mp3_found%"=="true" (
    echo MP3-Datei gefunden!
) else (
    echo Keine MP3-Datei gefunden.
)

if "%mp4_found%"=="true" (
    echo MP4-Datei gefunden!
) else (
    echo Keine MP4-Datei gefunden.
)
pause