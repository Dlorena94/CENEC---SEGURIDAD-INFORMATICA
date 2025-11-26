$action = New-ScheduledTaskAction -Execute 'calc.exe'

$trigger = New-ScheduledTaskTrigger -At 12:47 -Once

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'Abrircalculadora' -Description 'Abrir calculadora'
