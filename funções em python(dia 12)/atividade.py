
def calculadora():
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora...")
            break

        if opcao in ["1", "2", "3", "4"]:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))

                if opcao == "1":
                    resultado1 = num1 + num2
                    print(f"Resultado: {resultado1}")

                elif opcao == "2":
                    resultado2 = num1 - num2
                    print(f"Resultado: {resultado2}")

                elif opcao == "3":
                    resultado3 = num1 * num2
                    print(f"Resultado: {resultado3}")

                elif opcao == "4":
                     resultado4 = num1 / num2
                     print(f"Resultado: {resultado4}")
                