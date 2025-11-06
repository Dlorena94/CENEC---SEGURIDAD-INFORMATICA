Get-Process | Where-Object { $_.WorkingSet -gt 50MB }
