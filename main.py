def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

print("=== Calculadora em Python ===")

num1 = float(input("Primeiro número: "))
operacao = input("Operação (+, -, *, /): ")
num2 = float(input("Segundo número: "))

if operacao == "+":
    resultado = soma(num1, num2)
elif operacao == "-":
    resultado = subtracao(num1, num2)
elif operacao == "*":
    resultado = multiplicacao(num1, num2)
elif operacao == "/":
    resultado = divisao(num1, num2)
else:
    resultado = "Operação inválida."

print(f"Resultado: {resultado}")
