@echo off

REM Download and install Python
powershell -Command "& { iwr https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe -OutFile python-installer.exe }"
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Install required libraries
pip install bark scipy simpleaudio numpy

REM Run the Python script
python gorgeous.py