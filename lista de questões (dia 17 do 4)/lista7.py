def calculadora():
    while True:
        print("CALCULADORA")
        print("1 - Soma")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora...")
            break

        if opcao in ["1"]:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))

                if opcao == "1":
                    resultado1 = num1 + num2
                    print(f"Resultado: {resultado1}")
