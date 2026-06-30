@echo off
:: Dat bang ma UTF-8 cho CMD
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

:: Chuyen thu muc lam viec hien tai vao thu muc chua file bat nay
cd /d "%~dp0"

title Ve Bieu Do Gia PC - AI Dubbing
color 0E

echo =======================================================
echo KHOI DONG CONG CU VE BIEU DO GIA - AI DUBBING
echo =======================================================
echo.
echo Dang nap moi truong ao (Virtual Environment)...
call venv\Scripts\activate.bat

:: Kiem tra va cai dat matplotlib neu chua co
pip show matplotlib >nul 2>&1
if %errorlevel% neq 0 (
    echo Dang cai dat thu vien ve bieu do (matplotlib)...
    pip install matplotlib >nul
)

python ve_bieu_do_gia.py

echo.
echo =======================================================
echo HOAN THANH TIEN TRINH VE BIEU DO!
echo =======================================================
pause
