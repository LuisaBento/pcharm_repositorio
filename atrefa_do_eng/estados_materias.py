print("===== SISTEMA DE CONSULTA DE EQUIPAMENTOS =====")

equipamentos = {
    1: {
        "nome": "sansung",
        "Disponivel": True
    },
    2: {
        "nome": "nokia",
        "Emprestado": False
    },
    3: {
        "nome": "iphone",
        "Disponível": True
    },
    4: {
        "nome": "iphad",
        "Emprestado": False
    }
}

print("\nLISTA DE EQUIPAMENTOS")
print("----------------------------------------")
print("CÓDIGO | EQUIPAMENTO ")
print("----------------------------------------")

for codigo, equipamento in equipamentos.items():
    codigo = ""
    if codigo == True:
        print("Equipamento disponivel")
    nova_consulta = input("pretende efecuar uma nova consulta?  S/N")
    codigo = int(input("insira o codigo do material"))
    print(
        codigo, "|",
        equipamento["nome"],

    )

print("----------------------------------------")
