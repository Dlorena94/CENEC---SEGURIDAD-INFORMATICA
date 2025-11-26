param(
    # Hora de apagado en formato HH:mm (24h). Ejemplo: "23:30"
    [string]$hora = "10:00"
)

# --- 1. Definición de Variables de Tiempo ---

# Obtenemos la fecha y hora actual (solo para comparación)
$hoy = Get-Date

# Obtenemos la hora actual para modificar sus componentes (hora y minuto)
# El cmdlet Get-Date produce un objeto DateTime.
$apagado = $hoy

# Extraemos las partes de la hora (ej: "10" y "00")
$partes = $hora.Split(":")
$hora_set = [int]$partes[0]
$minuto_set = [int]$partes[1]

# Establecemos la hora y minuto del objeto $apagado para hoy, con segundos a cero.
# Usamos el método .AddHours y .AddMinutes para ajustar el tiempo con precisión.
# Primero, reseteamos el tiempo a la medianoche de hoy (00:00:00).
$apagado = $apagado.Date

# Luego, añadimos la hora y el minuto deseados.
$apagado = $apagado.AddHours($hora_set).AddMinutes($minuto_set)


# --- 2. Lógica de Fecha (Hoy o Mañana) ---

# Si la hora de apagado ya ha pasado hoy ($apagado es anterior o igual a $hoy),
# programamos el apagado para el mismo momento, pero mañana.
if ($apagado -le $hoy) {
    Write-Host "La hora de apagado $hora ya pasó hoy. Programando para mañana." -ForegroundColor Yellow
    $apagado = $apagado.AddDays(1)
}

# --- 3. Cálculo del Retraso en Segundos ---

# La diferencia entre el tiempo de apagado y el tiempo actual es un TimeSpan.
# Accedemos a la propiedad TotalSeconds de ese TimeSpan y lo convertimos a entero.
$tiempoRestante = $apagado - (Get-Date)
$segundos = [int]$tiempoRestante.TotalSeconds


# --- 4. Ejecución del Comando de Apagado ---

Write-Host "------------------------------------------------------------------"
Write-Host "✅ El equipo se apagará el $($apagado.ToString('dd/MM/yyyy')) a las $($apagado.ToString('HH:mm:ss'))" -ForegroundColor Green
Write-Host "   (Tiempo restante: $($tiempoRestante.Hours)h $($tiempoRestante.Minutes)m $($tiempoRestante.Seconds)s / $segundos segundos)" -ForegroundColor Green
Write-Host "------------------------------------------------------------------"

# Ejecutamos el comando shutdown.exe:
# /s: Apagado
# /t: Tiempo de espera en segundos
Start-Process -FilePath "shutdown.exe" -ArgumentList "/s", "/t", "$segundos" -NoNewWindow