@echo off
setlocal DisableDelayedExpansion
set "FS_DOCUMENTS="
for /f "usebackq delims=" %%D in (`powershell.exe -NoProfile -Command "[Environment]::GetFolderPath('MyDocuments')"`) do set "FS_DOCUMENTS=%%D"
if not defined FS_DOCUMENTS goto documents_failed
set "FS_EXTENSIONS=%FS_DOCUMENTS%\Inform\Extensions"
set "FS_PAYLOAD=%~dp0Extensions"
if not exist "%FS_EXTENSIONS%\" goto extensions_failed
if not exist "%FS_PAYLOAD%\" goto payload_failed
if not exist "%~dp0update-files.txt" goto payload_failed
for /f "usebackq delims=" %%F in ("%~dp0update-files.txt") do (call :preflight "%%F" || goto preflight_failed)
set "FS_BACKUP=%FS_DOCUMENTS%\Inform\PersonalModBackups\Exclusions-%RANDOM%-%RANDOM%"
if exist "%FS_BACKUP%\" goto backup_failed
mkdir "%FS_BACKUP%" || goto backup_failed
for /f "usebackq delims=" %%F in ("%~dp0update-files.txt") do (call :backup "%%F" || goto backup_failed)
for /f "usebackq delims=" %%F in ("%~dp0update-files.txt") do (call :install "%%F" || goto install_failed)
echo.
echo Updated 14 extensions. Backup: "%FS_BACKUP%"
echo Reopen your existing Inform project and click Release.
echo The modified game still needs to compile successfully.
pause
exit /b 0

:preflight
if not exist "%FS_PAYLOAD%\%~1" exit /b 1
if not exist "%FS_EXTENSIONS%\%~1" (
 echo Missing installed extension: "%FS_EXTENSIONS%\%~1"
 exit /b 1
)
exit /b 0

:backup
for %%P in ("%FS_BACKUP%\%~1") do if not exist "%%~dpP" mkdir "%%~dpP"
copy /y "%FS_EXTENSIONS%\%~1" "%FS_BACKUP%\%~1" >nul
exit /b %errorlevel%

:install
copy /y "%FS_PAYLOAD%\%~1" "%FS_EXTENSIONS%\%~1" >nul
exit /b %errorlevel%

:restore
copy /y "%FS_BACKUP%\%~1" "%FS_EXTENSIONS%\%~1" >nul
exit /b %errorlevel%

:install_failed
echo Update failed. Attempting to restore every extension from the backup.
set "FS_RESTORE_FAILED="
for /f "usebackq delims=" %%F in ("%~dp0update-files.txt") do (call :restore "%%F" || set "FS_RESTORE_FAILED=1")
if defined FS_RESTORE_FAILED (
 echo Restoration incomplete. Close Inform and copy the backup author folders into Extensions.
) else (
 echo Original extension files restored.
)
echo Backup: "%FS_BACKUP%"
pause
exit /b 1

:documents_failed
echo Could not locate your Documents folder.
goto failed
:extensions_failed
echo Could not find Inform Extensions at "%FS_EXTENSIONS%".
goto failed
:payload_failed
echo Extract the complete ZIP before running this installer.
goto failed
:preflight_failed
echo A required file is missing. No installed files were changed.
goto failed
:backup_failed
echo Backup could not be completed. No installed files were changed.
echo Backup location: "%FS_BACKUP%"
:failed
pause
exit /b 1
