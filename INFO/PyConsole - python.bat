@echo off
title PyConsole - installation

:uvitani
echo PyConsole - installation
echo version 2.1
echo c2023 by KralicekGamer
echo.
echo 1. Instalace
echo 2. Odejit
echo.
set /p volba="PyConsole@installation$ "

if "%volba%"=="2" goto exit
if "%volba%"=="1" goto kontrola_pythonu
goto uvitani

:kontrola_pythonu
python --version >nul 2>&1
if %errorlevel% neq 0 goto instalace_pythonu

echo Python je jiz nainstalovan
echo.
echo 1. Zkontrolovat znovu
echo 2. Exit
echo.
set /p volba="PyConsole@installation$ "

if "%volba%"=="1" goto kontrola_pythonu
if "%volba%"=="2" goto uspesna_instalace
goto kontrola_pythonu

:instalace_pythonu
echo Python nebyl nalezen na vasem systemu.
echo Chcete provest instalaci Pythonu? (ano/ne)
set /p volba="PyConsole@installation$ "

if /i "%volba%"=="ano" (
    start https://www.python.org/downloads/
    echo.
    echo Po dokonceni instalace stisknete Enter.
    pause
    goto kontrola_pythonu
) else (
    echo.
    echo Instalace pythonu zrusena
    echo.
    goto uvitani
)

:uspesna_instalace
echo Dekujeme
pause
exit

:exit
exit /b
