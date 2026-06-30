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
foreach ($r in $rams) {
    $sizeGB = [math]::Round($r.Capacity / 1GB, 2)
    $totalRam += $sizeGB
    Write-Log "    Thanh thu ${i}: ${sizeGB} GB | Toc do: $($r.Speed) MHz | Hang: $($r.Manufacturer) | Ma: $($r.PartNumber)" "White"
    $i++
}
Write-Log "    => TONG DUNG LUONG RAM: ${totalRam} GB" "Yellow"
Write-Log "" "White"

# 4. O cung (Disk)
Write-Log "[4] O CUNG LUU TRU (STORAGE) & TINH TRANG SUC KHOE" "Green"
$disks = Get-CimInstance Win32_DiskDrive
foreach ($d in $disks) {
    $sizeGB = [math]::Round($d.Size / 1GB, 2)
    Write-Log "    Ma Model: $($d.Model)  |  Dung luong: ${sizeGB} GB" "White"
    Write-Log "    Tinh trang SMART (Suc khoe): $($d.Status)" "Cyan"
}
Write-Log "" "White"

# 5. GPU
Write-Log "[5] CARD DO HOA (GPU)" "Green"
$gpus = Get-CimInstance Win32_VideoController
foreach ($g in $gpus) {
    Write-Log "    Ten Card (Windows nhan): $($g.Name)" "White"
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
Write-Log " => 3. Check RAM: Dung tong dung luong va Toc do MHz chua?" "White"
Write-Log " => 4. Check O CUNG: Tra Google ma Model xem phai loai chuan khong? SMART bao OK chua?" "White"
Write-Log " => 5. Check GPU: Co dung loai Card VRAM dung tich cao khong? VRAM NVIDIA bao chuan chua?" "White"
Write-Log " => 6. QUAN TRONG: Voi Nguon (PSU), Tan nhiet va Vo Case -> BAT BUOC KIEM TRA BANG MAT THUONG!" "Red"

Write-Log "" "White"
Write-Log "===========================================================" "Cyan"
Write-Log " DA LUU BIEN BAN VAO MAN HINH DESKTOP: BienBan_NghiemThu_AI_Dubbing.txt " "Yellow"
Write-Log "===========================================================" "Cyan"
Write-Log "" "White"
Read-Host "An Enter de thoat he thong..."
