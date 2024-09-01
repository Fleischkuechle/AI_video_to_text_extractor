rem this is are the arguments the script takes
@REM parser.add_argument("--video_path", type=str, default="", help="Path to the video file")
@REM     parser.add_argument("--output_name", type=str, default="output.txt", help="Name of the output text file")
@REM     parser.add_argument("--frame_rate", type=int, default=2, help="Desired frame rate (in seconds) e.g. 1 means it takes each second of the video a image and extracts the text from it.")
@REM     parser.add_argument("--tesseract_path", type=str, default=default_tesseract_path, help="Custom tesseract Path if you have pytesseract installed you also can use your custom pytesseract leave this empty and it will use its own.")
@REM     parser.add_argument("--headline", type=str, default=headline, help="Here you can add a headline that will appear in the output text file on top of the text like headlines ussually do.")

@REM @echo off

@REM call .venv\Scripts\activate


@echo off

cd /D "%~dp0"

set PATH=%PATH%;%SystemRoot%\system32

echo "%CD%"| findstr /C:" " >nul && echo This script relies on Miniconda which can not be silently installed under a path with spaces. && goto end

@rem fix failed install when installing to a separate drive
set TMP=%cd%\installer_files
set TEMP=%cd%\installer_files

@rem deactivate existing conda envs as needed to avoid conflicts
(call conda deactivate && call conda deactivate && call conda deactivate) 2>nul

@rem config
set CONDA_ROOT_PREFIX=%cd%\installer_files\conda
set INSTALL_ENV_DIR=%cd%\installer_files\env

@rem environment isolation
set PYTHONNOUSERSITE=1
set PYTHONPATH=
set PYTHONHOME=
set "CUDA_PATH=%INSTALL_ENV_DIR%"
set "CUDA_HOME=%CUDA_PATH%"

@rem activate installer env
call "%CONDA_ROOT_PREFIX%\condabin\conda.bat" activate "%INSTALL_ENV_DIR%" || ( echo. && echo Miniconda hook not found. && goto end )



echo to exit the programm close the terminal
:input_loop
REM Prompt the user for specific arguments
set /p arg1=Enter video_path or press enter to use default folder: 

if "%arg1%"=="" (
    set arg1="empty"
    echo using default folder .\user_data\output. will search for mp3 or mp4 files and process it.
)
@REM set /p arg2=Enter output_name or press enter to use default name: 

@REM if "%arg2%"=="" (
@REM     set arg2="empty"
@REM     echo using default output_name  default value is output.txt.
@REM )

set /p arg3=Enter frame_rate or press enter to use default : 

if "%arg3%"=="" (
    set arg3=2
    echo using default frame_rate. default value =2.
)

@REM REM Run the Python script with the specific arguments provided by the user
@REM python extract_fames.py %arg1% %arg2% %arg3%
@REM #python extract_fames.py --video_path "D:\47\02\AI_video_to_text_extractor\user_data\example_video.mp4" --output_name "output.txt" --frame_rate 2
REM Run the Python script with the specific arguments provided by the user
@REM python extract_fames.py --video_path %arg1% --output_name %arg2% --frame_rate %arg3%
python extract_fames.py --video_path %arg1%  --frame_rate %arg3%
pause