$nombre= Read-Host "¿Como te llamas?"
$edad= Read-Host "¿Cuantos años tienes?"

if ($edad -ge 18) {
    "$nombre es mayor de edad"
} else {
    "$nombre es menor de edad"
}