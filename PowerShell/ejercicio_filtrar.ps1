Get-Process |
Where-Object WorkingSet -gt 200MB |
Select-Object Name, Id, CPU, WorkingSet
| Export-Csv .\procesos_mayor200mb.csv -NoTypeInformation

