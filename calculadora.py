import math
import os
os.system("cls")

cal = input("Digite o calculo ")
partes =  cal.split()
resultado = 0

n1 = (float(partes[0]))
op = partes[1]
n2 = (float(partes[2])) if len(partes) > 2 else None

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "x":
 resultado = n1 * n2
elif op == "/":
  resultado = n1 / n2
elif op == "v":
   resultado = math.sqrt(n1) 
else:
   print("Operador inválido")
if resultado == math.sqrt(n1):
   print(f"{resultado : .2f}")
elif isinstance(resultado, float) and resultado.is_integer():
   print(int(resultado))
else:
   print(resultado)


    
