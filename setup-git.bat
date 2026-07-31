@echo off

echo Git Project Setup
echo.

set /p GIT_NAME=Git User Name :
set /p GIT_EMAIL=Git Email :
set /p USERNAME=GitHub Username :
set /p REPO=Repository Name :

git init
git config user.name "%GIT_NAME%"
git config user.email "%GIT_EMAIL%"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/%USERNAME%/%REPO%.git

echo.
echo Done!
pause