$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8

Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host " TỰ ĐỘNG THIẾT LẬP WINDOWS CHO PC AI DUBBING (CHẠY 24/7)   " -ForegroundColor Yellow
Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host "Script nay se tu dong tat cac tinh nang gay thet may cua Windows"
Write-Host "nhu Auto Update, Sleep, Hibernate..."
Write-Host ""

# 1. Disable Sleep and Hibernate
Write-Host "[1/4] Dang tat che do Ngu (Sleep) va Ngu dong (Hibernate)..." -ForegroundColor Green
powercfg -change -standby-timeout-ac 0
powercfg -change -standby-timeout-dc 0
powercfg -change -hibernate-timeout-ac 0
powercfg -change -hibernate-timeout-dc 0
powercfg -change -monitor-timeout-ac 0
powercfg -change -monitor-timeout-dc 0
powercfg -h off
Write-Host "    => Thanh cong." -ForegroundColor White

# 2. Set High Performance Power Plan
Write-Host "[2/4] Dang kich hoat che do Hieu nang cao (High Performance)..." -ForegroundColor Green
powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
Write-Host "    => Thanh cong." -ForegroundColor White

# 3. Disable Automatic Windows Update Restarts (Registry)
Write-Host "[3/4] Dang vo hieu hoa tinh nang tu dong khoi dong lai cua Windows Update..." -ForegroundColor Green
try {
    $registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
    if (!(Test-Path $registryPath)) {
        New-Item -Path $registryPath -Force | Out-Null
    }
    New-ItemProperty -Path $registryPath -Name "NoAutoRebootWithLoggedOnUsers" -Value 1 -PropertyType DWORD -Force | Out-Null
    Write-Host "    => Thanh cong. (Nho chu dong update Windows bang tay khi ban ranh roi)" -ForegroundColor White
} catch {
    Write-Host "    => Loi. Vui long chay script nay bang quyen Administrator (Run as Administrator)." -ForegroundColor Red
}

# 4. Nhac nho cai dat khac
Write-Host "[4/4] Khuyen nghi cai dat Driver..." -ForegroundColor Green
Write-Host "    => VOI NVIDIA: Hay cai dat ban [STUDIO DRIVER] thay vi ban [GAME READY DRIVER]." -ForegroundColor Magenta
Write-Host "       (Studio Driver on dinh hon, it bi loi Out of Memory khi chay AI 24/7)" -ForegroundColor Magenta
Write-Host "    => CONG CU THEO DOI: Khuyen nghi cai dat 'HWiNFO' de canh bao nhiet do GPU neu qua 85 do C." -ForegroundColor Magenta

Write-Host ""
Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host " HOAN TAT THIET LAP. MAY TINH SAN SANG CHAY 24/7.          " -ForegroundColor Yellow
Write-Host "===========================================================" -ForegroundColor Cyan
Read-Host "An Enter de thoat..."
