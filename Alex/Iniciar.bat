@echo off

:: Define the applications you want to open
set app1="C:\Users\minis\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Navegador Opera GX.lnk"
set app2="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
set app3="C:\Users\minis\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"


:: Open the applications
start "" %app1%
start "" %app2%
start "" %app3%

:: Clean up temporary files
echo Cleaning up temporary files...
del /F /S /Q /A:H C:\Windows\Temp\*
del /F /S /Q /A:H C:\Windows\Prefetch\*
del /F /S /Q /A:H %TEMP%\*
rd /S /Q %TEMP%\*

:: Empty the recycle bin
echo Emptying the recycle bin...
del /F /S /Q /A:H C:\$Recycle.Bin\*
rd /S /Q C:\$Recycle.Bin

echo Cleanup completed!