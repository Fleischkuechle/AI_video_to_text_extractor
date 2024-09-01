@echo off
REM Set the URL of the file to download
set "FILE_URL=https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe"

REM Set the destination path to the directory where the bat file is located
set "DESTINATION=%~dp0file.ext"

REM Download the file using curl
curl -o "%DESTINATION%" "%FILE_URL%"

REM Pause the script to view the output
pause
