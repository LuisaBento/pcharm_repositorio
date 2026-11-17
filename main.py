
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero!"
    return a / b


def potenciar(a, b):
    return a ** b


def mostrar_menu():
    print("\n========== CALCULADORA ==========")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("0. Sair")
    print("=================================")


def executar_calculadora():
    while True:
        mostrar_menu()

        opcao = input("Escolha uma operação: ")

        if opcao == "0":
            print("Calculadora encerrada. Até breve!")
            break

        if opcao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            numero1 = float(input("Introduza o primeiro número: "))
            numero2 = float(input("Introduza o segundo número: "))
        except ValueError:
            print("Erro: introduza apenas valores numéricos.")
            continue

        if opcao == "1":
            resultado = somar(numero1, numero2)

        elif opcao == "2":
            resultado = subtrair(numero1, numero2)

        elif opcao == "3":
            resultado = multiplicar(numero1, numero2)

        elif opcao == "4":
            resultado = dividir(numero1, numero2)

        elif opcao == "5":
            resultado = potenciar(numero1, numero2)

        print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    executar_calculadora()
