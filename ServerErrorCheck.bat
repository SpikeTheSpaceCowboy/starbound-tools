@echo off
set number=0

:errorcheck
netstat -o -n -a | findstr [Local Server IP]:21025 | findstr CLOSE-WAIT
if %ERRORLEVEL% equ 0 (goto killserver) ELSE (goto waiting)

:running
echo Server is Running
echo %number% Restarts today.
if not "%number%" == "0" echo Last Restarted %restarttime%
timeout /t 30 /nobreak
goto errorcheck

:waiting
netstat -o -n -a | findstr [Local Server IP]:21025 | findstr ESTABLISHED
if %ERRORLEVEL% equ 0 (goto running) ELSE (goto tryagain)

:tryagain
timeout /t 30 /nobreak
goto errorcheck

:killserver
killtask starbound_server.exe
timeout /t 10 /nobreak
set /a number=number+1
set cur_hh=%time:~0,2%
if %cur_hh% lss 10 (set cur_hh=0%time:~1,1%)
set cur_nn=%time:~3,2%
set cur_ss=%time:~6,2%
set cur_yyyy=%date:~10,4%
set cur_mm=%date:~4,2%
set cur_dd=%date:~7,2%
set timestamp=%cur_hh%:%cur_nn%:%cur_ss% - %cur_mm%/%cur_dd%/%cur_yyyy%
set restarttime=%timestamp%
goto serverrestart

:serverrestart
start ~\ServerRestart.bat
ping 127.0.0.1 -n 1
goto wait

:wait
timeout /t 60 /nobreak
echo Server Restarted
goto errorcheck
