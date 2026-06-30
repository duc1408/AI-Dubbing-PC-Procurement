$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8

# Chuan bi file xuat ra Desktop
$desktopPath = [Environment]::GetFolderPath("Desktop")
$logFile = "$desktopPath\BienBan_NghiemThu_AI_Dubbing.txt"

Function Write-Log {
    param([string]$text, [string]$color="White")
    Write-Host $text -ForegroundColor $color
    Add-Content -Path $logFile -Value $text -Encoding UTF8
}

Clear-Content -Path $logFile -ErrorAction SilentlyContinue

Write-Log "===========================================================" "Cyan"
Write-Log "    HE THONG KIEM TRA PHAN CUNG NGHIEM THU AI DUBBING      " "Yellow"
Write-Log "===========================================================" "Cyan"
Write-Log "Muc dich: Doi chieu chong gian lan phan cung khi nhan may." "White"
Write-Log "Thoi gian kiem tra: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')" "White"
Write-Log "" "White"

# 0. OS Info
Write-Log "[0] HE DIEU HANH (WINDOWS)" "Green"
$os = Get-CimInstance Win32_OperatingSystem
Write-Log "    Phien ban: $($os.Caption) ($($os.OSArchitecture))" "White"
Write-Log "    Ngay cai dat: $($os.InstallDate)" "White"

$installAge = (Get-Date) - $os.InstallDate
if ($installAge.TotalDays -gt 30) {
    Write-Log "    => CANH BAO: Windows duoc cai dat tu $([int]$installAge.TotalDays) ngay truoc. SSD co the la hang cu hoac dung ban Ghost/Clone!" "Red"
} else {
    Write-Log "    => Trang thai OS: Cai dat moi (Tu $([int]$installAge.TotalDays) ngay truoc)" "Cyan"
}
Write-Log "" "White"

# 1. CPU
Write-Log "[1] BO VI XU LY (CPU)" "Green"
$cpu = Get-CimInstance Win32_Processor
foreach ($c in $cpu) {
    Write-Log "    Ten CPU: $($c.Name)" "White"
    Write-Log "    So Nhan (Cores): $($c.NumberOfCores) / So Luong (Threads): $($c.NumberOfLogicalProcessors)" "White"
}
Write-Log "" "White"

# 2. Mainboard
Write-Log "[2] BO MACH CHU (MAINBOARD)" "Green"
$main = Get-CimInstance Win32_BaseBoard
Write-Log "    Hang san xuat: $($main.Manufacturer)" "White"
Write-Log "    Ma san pham: $($main.Product)" "White"
Write-Log "" "White"

# 3. RAM
Write-Log "[3] BO NHO TRONG (RAM)" "Green"
$rams = Get-CimInstance Win32_PhysicalMemory
$totalRam = 0
$i = 1
$ramSpeeds = @()
foreach ($r in $rams) {
    $sizeGB = [math]::Round($r.Capacity / 1GB, 2)
    $totalRam += $sizeGB
    Write-Log "    Thanh thu ${i}: ${sizeGB} GB | Toc do: $($r.Speed) MHz | Hang: $($r.Manufacturer) | Ma: $($r.PartNumber)" "White"
    $ramSpeeds += $r.Speed
    $i++
}
Write-Log "    => TONG DUNG LUONG RAM: ${totalRam} GB" "Yellow"

if ($rams.Count -gt 1) {
    Write-Log "    => Trang thai RAM: Dang chay Dual/Quad Channel (Tot)" "Cyan"
} else {
    Write-Log "    => CANH BAO: Chi co 1 thanh RAM (Single Channel), lam giam hieu nang he thong!" "Red"
}

$highSpeedCount = ($ramSpeeds | Where-Object { $_ -gt 5600 }).Count
if ($highSpeedCount -gt 0) {
    Write-Log "    => CANH BAO XMP: Phat hien bus RAM > 5600MHz. Dam bao cua hang KHONG bat XMP/EXPO de tranh man hinh xanh khi treo 24/7!" "Red"
}
Write-Log "" "White"

# 4. O cung (Disk)
Write-Log "[4] O CUNG LUU TRU (STORAGE) & TINH TRANG SUC KHOE" "Green"
$disks = Get-CimInstance Win32_DiskDrive
foreach ($d in $disks) {
    $sizeGB = [math]::Round($d.Size / 1GB, 2)
    Write-Log "    Ma Model: $($d.Model)  |  Dung luong: ${sizeGB} GB" "White"
    Write-Log "    Tinh trang SMART (Suc khoe): $($d.Status)" "Cyan"
}
Write-Log "    => Dang tai cong cu kiem tra SSD chuyen sau (CrystalDiskInfo) de check gio chay/TBW..." "Yellow"
$cdiZip = "$env:TEMP\CrystalDiskInfo.zip"
$cdiFolder = "$env:TEMP\CrystalDiskInfo"
try {
    Invoke-WebRequest -Uri "https://github.com/hiyohiyo/CrystalDiskInfo/releases/download/9.2.2/CrystalDiskInfo9_2_2.zip" -OutFile $cdiZip -ErrorAction Stop
    Expand-Archive -Path $cdiZip -DestinationPath $cdiFolder -Force
    Write-Log "    => Da tai xong CrystalDiskInfo." "Cyan"
    Write-Log "    [!] HAY MO THU MUC: $cdiFolder VA CHAY FILE DiskInfo64.exe DE XEM SO GIO CHAY / TBW CUA SSD!" "Magenta"
} catch {
    Write-Log "    (Loi khi tai CrystalDiskInfo. Vui long tu tai thu cong de check so gio chay cua SSD)" "DarkGray"
}
Write-Log "" "White"

# 5. GPU
Write-Log "[5] CARD DO HOA (GPU)" "Green"
$gpus = Get-CimInstance Win32_VideoController
foreach ($g in $gpus) {
    Write-Log "    Ten Card (Windows nhan): $($g.Name)" "White"
    # Lay luon dung luong VRAM tu WMI de doi chieu voi NVIDIA
    if ($g.Name -match "NVIDIA") {
        $wmiVRAMGB = [math]::Round($g.AdapterRAM / 1GB, 1)
        if ($wmiVRAMGB -gt 0) {
            Write-Log "    VRAM (WMI Windows doc duoc): ${wmiVRAMGB} GB" "Cyan"
        }
    }
}

try {
    $nvidia = & nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>$null
    if ($nvidia) {
        Write-Log "    Thong tin VRAM thuc te tu NVIDIA Chip:" "Cyan"
        foreach ($line in $nvidia) {
            Write-Log "    => $line" "Yellow"
        }
    }
} catch {
    Write-Log "    (Luu y: Chua cai Driver NVIDIA nen chua soi duoc VRAM thuc)" "DarkGray"
}

Write-Log "" "White"
Write-Log "===========================================================" "Cyan"
Write-Log " [!] CHECKLIST DOI CHIEU VOI BAO GIA BAN DAU" "Magenta"
Write-Log "===========================================================" "Cyan"
Write-Log " => 1. Check CPU: Dung the he, dung so nhan/luong chua?" "White"
Write-Log " => 2. Check MAINBOARD: Dung ten Hang va Ma Hau To chua?" "White"
Write-Log " => 3. Check RAM: Dung tong dung luong va Toc do MHz chua? Phai bao Dual Channel!" "White"
Write-Log " => 4. Check O CUNG: Tra Google ma Model xem phai loai chuan khong? Tinh trang Windows co the hien la cai tren o cu?" "White"
Write-Log " => 5. Check GPU: Co dung loai Card VRAM dung tich cao khong? VRAM NVIDIA bao chuan chua?" "White"
Write-Log " => 6. QUAN TRONG: Voi Nguon (PSU) -> BAT BUOC MO NAP CASE KIEM TRA BANG MAT THUONG ten Hang, 80 Plus Gold!" "Red"
Write-Log " => 7. QUAN TRONG: Yeu cau cua hang chay FURMARK hoac OCCT test 15 phut de kiem tra Nguon va Nhiet do!" "Red"

Write-Log "" "White"
Write-Log "===========================================================" "Cyan"
Write-Log " DA LUU BIEN BAN VAO MAN HINH DESKTOP: BienBan_NghiemThu_AI_Dubbing.txt " "Yellow"
Write-Log "===========================================================" "Cyan"
Write-Log "" "White"
Read-Host "An Enter de thoat he thong..."
