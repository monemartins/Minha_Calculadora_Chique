#Minha Calculadora Chique.py
#26.08.14
#By Simone Martins -  https://github.com/monemartins

# Importa "os" que permite executar comandos do sistema

import os

def cls():
    #limpa a tela
    if os.name == "nt":
        #Se o sistema for Windows
        os.system("cls")
    else:
        #outros sistemas com Linux e MacOS
        os.system("clear")

def somar(val1, val2):
    return val1 + val2

def subtrair(val1, val2):
    return val1 - val2

def multiplicar(val1, val2):
    return val1 * val2

def dividir(val1, val2):
    if val2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return val1 / val2

#Estrutura da Calculadora

def calculadora():
    while True:
        print("\n=== MINHA CALCULADORA CHIQUE")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("0. Sair")

# Escolha da opção do cálculo matemático
        
        opcao = input("\nEscolha uma opção (0-4): ")
        
        if opcao == '0':
            print("Encerrando a calculadora. Até logo!")
            break
            
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
                continue
            #para resultado com número inteiro
                #num1 = int(input("Digite o primeiro número: "))
                #num2 = int(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = somar(num1, num2)
                simbolo = "+"
            elif opcao == '2':
                resultado = subtrair(num1, num2)
                simbolo = "-"
            elif opcao == '3':
                resultado = multiplicar(num1, num2)
                simbolo = "*"
            elif opcao == '4':
                resultado = dividir(num1, num2)
                simbolo = "/"

            if isinstance(resultado, str):
                print(f"\n{resultado}")
            else:
                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")
        else:
            print("Opção inválida! Escolha um número entre 0 e 4.")

# Executa o programa
calculadora()