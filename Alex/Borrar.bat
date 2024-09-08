@echo off
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