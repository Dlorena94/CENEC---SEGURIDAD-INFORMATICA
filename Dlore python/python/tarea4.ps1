$action = New-ScheduledTaskAction -Execute 'explorer.exe'

$trigger = New-ScheduledTaskTrigger -At 12:46 -Once

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'Abrirexplorer' -Description 'Abrir explorer'
