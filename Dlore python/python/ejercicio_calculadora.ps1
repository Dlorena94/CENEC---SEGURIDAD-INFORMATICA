$tabla= Read-Host "Ingresa el número para la tabla de multiplicar"

$numeros= 1..10

foreach ($n in $numeros){
    $resultado = $n * $tabla
    Write-Host "Numero: $n x $tabla = $resultado"
}

Write-Host ""
Write-Host "Fin"