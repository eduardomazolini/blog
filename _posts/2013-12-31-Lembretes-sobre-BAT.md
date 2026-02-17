---
---


```
@echo off
TITLE NAO FECHAR EXECUTANDO
cd /d %~dp0
SETLOCAL ENABLEEXTENSIONS
SETLOCAL ENABLEDELAYEDEXPANSION
start /w notepad.exe
:: Comentario
rem Comentario
timeout /t 10 /nobreak
goto label
echo nao vai executar
:label
call :wait 5
exit /b 0
:wait
ping 127.0.0.1 -n %1
goto :EOF
```
