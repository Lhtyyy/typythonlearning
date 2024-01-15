@echo off


echo install and upgrade the requires
python -m pip install --upgrade setuptools wheel twine

python setup.py sdist bdist_wheel
if %errorlevel% neq 0 (
    echo Fail to package
    pause || EXIT /b 1
)

python -m twine upload --repository testpypi dist/*
pause