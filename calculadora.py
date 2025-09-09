import math
import os
os.system("cls")

entrada = input("Digite sua conta: ")
partes = entrada.split()
resultado = 0

n1 = float(partes[0])
op = partes[1]
n2 = float(partes[2]) if len(partes) > 2 else None

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op in ["x", "×", "*"]:
    resultado = n1 * n2
elif op in ["/", "÷"]:
    if n2 == 0:
        resultado = "Erro"
    elif n1.is_integer() and n2.is_integer():  
        resultado = f"{int(n1 // n2)} (resto {int(n1 % n2)})"
    else:
        resultado = n1 / n2
elif op in ["√", "v"]:  
    resultado = math.sqrt(n1)
else:
    resultado = "Operador inválido!"

if isinstance(resultado, float) and resultado.is_integer():
    print(int(resultado))
else:
    print(resultado if isinstance(resultado, str) else f"{resultado:.2f}")
