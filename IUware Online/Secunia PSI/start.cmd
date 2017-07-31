echo OFF
cls
echo Step 1 of 2: Installing PSI
echo.
echo *******************************
echo * Please do not close this    *
echo * window during installation. *
echo *******************************
PSISetup.exe
rem pause

cls
echo Step 2 of 2: Installing CSI
echo.
echo *******************************
echo * Please do not close this    *
echo * window during installation. *
echo *******************************

msiexec /i "AgentInstaller.msi"

cls
echo Installation Complete
start wscript complete.vbs
exit