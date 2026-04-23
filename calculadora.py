def calcular ():
    while True:
        print("\n Calculadora")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Escolha uma opção:")
        if opcao == "5":
            print("Encerrado.")
            break
        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue
        try:
            num1 = float(input("Digite o primeiro número:"))
            num2 = float(input("Digite o segundo número:"))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue
        if opcao == "1":
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
            
            
calcular()
