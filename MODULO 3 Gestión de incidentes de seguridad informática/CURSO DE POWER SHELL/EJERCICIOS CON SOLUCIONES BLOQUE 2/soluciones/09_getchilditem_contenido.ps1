# SOLUCIÓN 9
Get-ChildItem C:\Logs -Filter *.txt -Recurse | Select-String -Pattern "ERROR"
