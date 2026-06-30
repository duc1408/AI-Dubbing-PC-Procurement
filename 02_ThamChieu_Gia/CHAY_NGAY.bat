@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0"

title [AI Dubbing] He Thong Tham Chieu Gia PC - V6

:: ============================================================
:: BUOC 0: KIEM TRA PYTHON
:: ============================================================
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo  [LOI] Chua cai dat Python tren may tinh nay!
    echo.
    echo  Vui long vao dia chi sau de tai Python:
    echo  https://www.python.org/downloads/
    echo.
    echo  Sau khi cai xong, chay lai file nay.
    pause
    exit /b 1
)

:: ============================================================
:: BUOC 1: KIEM TRA VA THIET LAP MOI TRUONG AO (VENV)
:: ============================================================
if not exist "venv\Scripts\activate.bat" (
    echo.
    echo  [THIET LAP LAN DAU] Dang tao moi truong lam viec...
    echo  ^(Viec nay chi lam 1 lan duy nhat, mat khoang 2-3 phut^)
    echo.
    python -m venv venv
    if errorlevel 1 (
        echo  [LOI] Khong the tao moi truong ao. Kiem tra lai Python.
        pause & exit /b 1
    )
    call venv\Scripts\activate.bat
    echo  Dang cai dat thu vien can thiet...
    pip install --quiet -r requirements.txt
    echo  Dang cai dat trinh duyet tu dong (Playwright)...
    playwright install chromium --quiet
    echo.
    echo  [OK] Thiet lap hoan tat!
) else (
    call venv\Scripts\activate.bat
)

:: ============================================================
:: MENU CHINH
:: ============================================================
:MENU
cls
echo.
echo  ================================================================
echo    HE THONG THAM CHIEU GIA PC AI DUBBING
echo    Phien ban V6 — Da sua Bug cao gia + Tich hop Du toan
echo  ================================================================
echo.
echo    [1]  Cao gia moi nhat (chay ~5-10 phut)
echo    [2]  Ve bieu do xu huong gia lich su
echo    [3]  CAO GIA + VE BIEU DO ^(Khuyen nghi^)
echo    [4]  Thoat
echo.
echo  ================================================================
set /p choice="   Chon tuy chon (1-4): "

if "%choice%"=="1" goto :SCRAPE
if "%choice%"=="2" goto :CHART
if "%choice%"=="3" goto :BOTH
if "%choice%"=="4" exit /b 0
echo  [!] Lua chon khong hop le. Vui long chon lai.
timeout /t 2 >nul
goto :MENU

:SCRAPE
echo.
echo  ================================================================
echo   DANG CAO GIA - Vui long cho ~5-10 phut...
echo   (Chuong trinh dang truy cap 6 trang ban le PC lon nhat VN)
echo  ================================================================
echo.
python cong_cu_cao_gia_tu_dong.py
echo.
echo  ================================================================
echo   HOAN TAT! Ket qua da luu trong thu muc: data\
echo  ================================================================
pause
goto :MENU

:CHART
echo.
echo  ================================================================
echo   DANG VE BIEU DO XU HUONG GIA...
echo  ================================================================
echo.
python ve_bieu_do_gia.py
echo.
echo  ================================================================
echo   HOAN TAT! Bieu do da luu: data\bieu_do_gia.png
echo  ================================================================
pause
goto :MENU

:BOTH
echo.
echo  ================================================================
echo   BUOC 1/2: DANG CAO GIA...
echo  ================================================================
echo.
python cong_cu_cao_gia_tu_dong.py
echo.
echo  ================================================================
echo   BUOC 2/2: DANG VE BIEU DO...
echo  ================================================================
echo.
python ve_bieu_do_gia.py
echo.
echo  ================================================================
echo   HOAN TAT TOAN BO!
echo   - Bao cao gia:    data\ket_qua_cao_gia_[ngay_gio].md
echo   - Du toan PC:     data\gia_tham_chieu_tong_the_[ngay_gio].md
echo   - Bieu do:        data\bieu_do_gia.png
echo  ================================================================
pause
goto :MENU
