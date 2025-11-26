$action = New-ScheduledTaskAction -Execute 'notepad.exe'

$trigger = New-ScheduledTaskTrigger -At 12:35 -Once


Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'AbrirNotepad' -Description 'Abrir Notepad al mediodía'
