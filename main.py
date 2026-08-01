continuar = "s"

while continuar == "s":

    print("=== Calculadora Python ===")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Opção: ")

    if opcao == "1":
        print("Resultado:", num1 + num2)

    elif opcao == "2":
        print("Resultado:", num1 - num2)

    elif opcao == "3":
        print("Resultado:", num1 * num2)

    elif opcao == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Não é possível dividir por zero.")

    else:
        print("Opção inválida.")

    continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()

print("\nObrigado por usar a calculadora!")
