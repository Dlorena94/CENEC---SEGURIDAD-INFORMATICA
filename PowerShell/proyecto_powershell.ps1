Write-Host "--- Iniciando la generación de informes ---" -ForegroundColor Yellow

$RutaProcesos = "C:\Informes\Procesos"
$RutaServicios = "C:\Informes\Servicios"
$LimiteMemoriaBytes = 150 * 1024 * 1024

Write-Host "Creando la estructura de carpetas: C:\Informes..." -ForegroundColor Cyan

New-Item -Path $RutaProcesos -ItemType Directory -Force -ErrorAction SilentlyContinue | Out-Null
New-Item -Path $RutaServicios -ItemType Directory -Force -ErrorAction SilentlyContinue | Out-Null

Write-Host "1/2: Filtrando procesos de alto consumo..." -ForegroundColor Cyan

$ProcesosFiltrados = Get-Process -ErrorAction SilentlyContinue |
    Where-Object { $_.WorkingSet -gt $LimiteMemoriaBytes } |
    Select-Object Name, Id, CPU, @{
        Name = "Memoria_MB"
        Expression = { "{0:N2}" -f ($_.WorkingSet / 1MB) }
    }

$ConteoProcesos = $ProcesosFiltrados.Count
$ArchivoProcesosCSV = "$RutaProcesos\procesos.csv"
$ProcesosFiltrados | Export-Csv -Path $ArchivoProcesosCSV -NoType

Write-Host "2/2: Filtrando servicios detenidos..." -ForegroundColor Cyan

$ServiciosDetenidos = Get-Service |
    Where-Object { $_.Status -eq "Stopped" } |
    Select-Object Name, DisplayName, Status

$ConteoServicios = $ServiciosDetenidos.Count
$ArchivoServiciosTXT = "$RutaServicios\servicios.txt"

$ServiciosDetenidos | Format-Table -AutoSize | Out-String | Out-File -FilePath $ArchivoServiciosTXT -Encoding UTF8 -Force

Write-Host "Procesos exportados (> 150 MB): $ConteoProcesos" -ForegroundColor White
Write-Host "Servicios detenidos exportados: $ConteoServicios" -ForegroundColor White
Write-Host "Archivos guardados en C:\Informes" -ForegroundColor White
