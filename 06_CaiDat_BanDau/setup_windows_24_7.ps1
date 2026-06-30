$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8

# Yeu cau quyen Administrator (Auto-Elevate)
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Dang yeu cau quyen Administrator de thi thiet lap he thong..." -ForegroundColor Yellow
    Start-Process PowerShell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

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

# 3. Disable Automatic Windows Update Restarts & Driver Overwrite (Registry)
Write-Host "[3/4] Dang vo hieu hoa tu dong khoi dong lai va can thiep Driver cua Windows Update..." -ForegroundColor Green
try {
    # 3A. Chan tu dong restart
    $registryPathAU = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
    if (!(Test-Path $registryPathAU)) {
        New-Item -Path $registryPathAU -Force | Out-Null
    }
    New-ItemProperty -Path $registryPathAU -Name "NoAutoRebootWithLoggedOnUsers" -Value 1 -PropertyType DWORD -Force | Out-Null
    
    # 3B. Chan Windows Update tu dong cai de Driver (vi du: de Driver NVIDIA cu chong len Studio Driver)
    $registryPathWU = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"
    if (!(Test-Path $registryPathWU)) {
        New-Item -Path $registryPathWU -Force | Out-Null
    }
    New-ItemProperty -Path $registryPathWU -Name "ExcludeWUDriversInQualityUpdate" -Value 1 -PropertyType DWORD -Force | Out-Null
    
    Write-Host "    => Thanh cong. (Da chan Windows tu dong restart va tu dong cai de Driver)" -ForegroundColor White
} catch {
    Write-Host "    => Loi khi ghi Registry. Vui long kiem tra lai quyen Administrator." -ForegroundColor Red
}

# 4. Nhac nho cai dat khac
Write-Host "[4/4] Khuyen nghi cai dat Driver va BIOS..." -ForegroundColor Green
Write-Host "    => VOI NVIDIA: Hay cai dat ban [STUDIO DRIVER] thay vi ban [GAME READY DRIVER]." -ForegroundColor Magenta
Write-Host "       (Studio Driver on dinh hon, it bi loi Out of Memory khi chay AI 24/7)" -ForegroundColor Magenta
Write-Host "    => TRONG BIOS: Ban hay khoi dong lai may vao BIOS, tim muc 'Restore on AC/Power Loss' va bat thanh [Power On]." -ForegroundColor Magenta
Write-Host "       (De khi bi cup dien va co dien lai, may se tu dong bat len ma khong can bam nut nguon)" -ForegroundColor Magenta
Write-Host "    => CONG CU THEO DOI: Khuyen nghi cai dat 'HWiNFO' de canh bao nhiet do GPU neu qua 85 do C." -ForegroundColor Magenta

Write-Host ""
Write-Host "===========================================================" -ForegroundColor Cyan
Write-Host " HOAN TAT THIET LAP. MAY TINH SAN SANG CHAY 24/7.          " -ForegroundColor Yellow
Write-Host "===========================================================" -ForegroundColor Cyan
Read-Host "An Enter de thoat..."
