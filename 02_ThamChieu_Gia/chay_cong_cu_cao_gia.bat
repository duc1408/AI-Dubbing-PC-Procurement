@echo off
:: Dat bang ma UTF-8 cho CMD
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

:: Chuyen thu muc lam viec hien tai vao thu muc chua file bat nay (docs)
cd /d "%~dp0"

title He Thong Check Gia PC AI Dubbing
echo =======================================================
echo KHOI DONG HE THONG CHECK GIA PC - AI DUBBING
echo =======================================================
echo.
echo Dang nap moi truong ao (Virtual Environment)...

:: Kich hoat moi truong ao (vi da cd vao docs roi nen goi truc tiep venv)
call venv\Scripts\activate.bat
python check_pc_prices.py

echo.
echo =======================================================
echo HOAN THANH TIEN TRINH QUET GIA!
echo =======================================================
pause
