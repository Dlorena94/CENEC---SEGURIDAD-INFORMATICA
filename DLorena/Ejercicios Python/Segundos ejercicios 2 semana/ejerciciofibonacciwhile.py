valor1=0
valor2=1
contador=0
limite=11

print("Serie:")

while contador < limite:
   print(valor1)
   siguiente = valor1+valor2
   valor1=valor2
   valor2=siguiente
   contador += 1
   