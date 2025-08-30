n1 = float(input("O primeiro número é: "))
operador = (input("O operador é: "))
n2 = float(input("O segundo número é: "))

if operador == "+":
 print(n1 + n2)
elif operador == "-":
 print(n1 - n2)
elif operador == "x":
 print(n1 * n2) 
elif operador == "/":
 print(n1 / n2)
else:
 print("Erro")