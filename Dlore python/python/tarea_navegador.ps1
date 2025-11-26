$action = New-ScheduledTaskAction -Execute 'msedge.exe'

$trigger = New-ScheduledTaskTrigger -At 12:45 -Once

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'Abrirmsedge' -Description 'Abrir msedge'


