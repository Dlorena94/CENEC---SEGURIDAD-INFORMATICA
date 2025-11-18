Get-Service |
  Where-Object Status -eq 'Stopped' |
  Select-Object Name, DisplayName, Status |
  Out-File .\servicios_detenidos.txt -Encoding utf8

  Get-Service | Out-File servicios.txt