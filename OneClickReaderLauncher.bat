@echo off
if "%~1"=="-background" goto :run

:: Create a temporary script to relaunch this batch file invisibly
echo Set WshShell = CreateObject("WScript.Shell") > "%temp%\hide.vbs"
echo WshShell.Run """" ^& WScript.Arguments(0) ^& """ -background", 0, False >> "%temp%\hide.vbs"
wscript "%temp%\hide.vbs" "%~f0"
del "%temp%\hide.vbs"
exit

:run
:: Your actual payload runs below this line in the background
cd /d "%~dp0"
call ..\venv\Scripts\activate
python main.py











::@echo off
::call ..\venv\Scripts\activate
::python main.py
::pause
