
New-Item -Path C:\Informes\Archivos -ItemType Directory

New-Item -Path C:\Informes\Servicios -ItemType Directory

Get-Process |
Where-Object WorkingSet -gt 50MB |
Select-Object WorkingSet, Id

Get-Service |
 Where-Object Status -eq 'Running' |
 Select-Object Name, DisplayName, Status |
 Out-File .\servicios_activos.txt -Encoding utf8
 
 Get-Service | Out-File .\servicios.txt