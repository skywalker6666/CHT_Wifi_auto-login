# 設置日誌文件的路徑
$logFilePath = "C:\Users\alan9\SideProjects\CHT_Wifi_auto-login\logfile.txt"

# 定義一個函數來寫入日誌
function Write-Log {
    param (
        [string]$logMessage
    )
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $logMessageWithTimestamp = "$timestamp - $logMessage"
    Add-Content -Path $logFilePath -Value $logMessageWithTimestamp
}

# 寫入開始執行訊息
Write-Log "start to exec WifiLogin.py"

# 執行 Python 腳本
try {
    python "C:\Users\alan9\SideProjects\CHT_Wifi_auto-login\WifiLogin.py"
    Write-Log "WifiLogin.py executed successfully."
} catch {
    Write-Log "exec WifiLogin.py with errors: $_"
}

# 寫入結束執行訊息
Write-Log "finish execution"