from main import somar, subtrair, multiplicar, dividir, potenciar

def testar_somar():
    assert somar(10, 5) == 15

def testar_subtrair():
    assert subtrair(10, 5) == 5

def testar_multiplicar():
    assert multiplicar(10, 5) == 50

def testar_dividir():
    assert dividir(10, 5) == 2

def testar_potenciar():
    assert potenciar(2, 3) == 8


testar_somar()
testar_subtrair()
testar_multiplicar()
testar_dividir()
testar_potenciar()

print("Todos os testes foram executados com sucesso!")