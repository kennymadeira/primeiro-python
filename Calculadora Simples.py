while True:
    print("--Calculadora Básica--")
    print("Escolha a opção desejada:")
    print("1-Soma")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão") 
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        resultado = numero1 + numero2
        print("O resultado da soma é:", resultado)
    elif opcao == 2:
        resultado = numero1 - numero2
        print("O resultado da subtração é:", resultado)
    elif opcao == 3:
        resultado = numero1 * numero2
        print("O resultado da multiplicação é:", resultado)
    elif opcao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print("O resultado da divisão é:", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")
            if opcao < 1 or opcao > 4:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                continue
            break