$action = New-ScheduledTaskAction -Execute 'githubdesktop'

$trigger = New-ScheduledTaskTrigger -At 12:56 -Once

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'Abrigithub' -Description 'Abrir github desktop'