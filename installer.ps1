$executablePath = "C:\Windows\System32\YourExecutable.exe"

icacls $executablePath /grant Users:RX

$taskDateTime = "2023-10-01 14:30"
$taskTime = [DateTime]::ParseExact($taskDateTime, "yyyy-MM-dd HH:mm", $null)
$trigger = New-ScheduledTaskTrigger -Once -At $taskTime
$action = New-ScheduledTaskAction -Execute $executablePath -Argument $arguments
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "MyTask" -Description "My Scheduled Task Description" -User "USERNAME" -Password "PASSWORD"