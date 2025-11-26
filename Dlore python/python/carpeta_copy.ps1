New-Item -Path C:\Backup -ItemType Directory

New-Item -Path C:\Final -ItemType Directory

Copy-Item C:\Reportes\resumen.txt C:\Backup

Move-Item C:\Backup\resumen.txt C:\Final  