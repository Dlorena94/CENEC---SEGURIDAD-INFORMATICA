# SOLUCIÓN 10
Get-ChildItem C:\Users\Public -Recurse | Group-Object Extension | Select-Object Name,Count
