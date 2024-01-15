@echo off
set VIRTUAL_VENV=%cd%\..\venv
set REQUIREMENTS_FILEPATH=%cd%\..\requirements.txt

echo To setup python virtual environment under the directory:
echo %VIRTUAL_VENV%

set PYTHON_CMD=python
%PYTHON_CMD% --version
if %errorlevel% neq 0 (
    echo Fail to execute python command, please check environment
    pause || EXIT /b 1
)

if EXIST %VIRTUAL_VENV% (
    echo venv directory is exist, remove it first
    rd /s/q %VIRTUAL_VENV%
)

echo Start to create python virtual environment
%PYTHON_CMD% -m venv %VIRTUAL_VENV%
if %errorlevel% neq 0 (
    echo Fail to create python virtual environment
    pause || EXIT /b 1
)

set "PATH=%VIRTUAL_VENV%/Scripts;%PATH%"
python -m pip install --upgrade pip
python -m pip install -r %REQUIREMENTS_FILEPATH% -i https://pypi.tuna.tsinghua.edu.cn/simple
pause