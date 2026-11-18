
print("BEM-VINDO À LOJA DE EMPRÉSTIMOS BENTO")

materiais = {
    "1": {"nome": "Computador HP", "disponivel": True},
    "2": {"nome": "Computador Dell", "disponivel": False},
    "3": {"nome": "Computador Lenovo", "disponivel": True},
    "4": {"nome": "Computador Dell Latitude", "disponivel": True},


}

registos = []

nome_usuario = ""
nome_fornecedor = ""

while True:

    print("\nMateriais disponíveis:")

    for codigo, material in materiais.items():
        print(codigo, "-", material["nome"])

    codigo = input("\nDigite o código do material: ")

    if codigo not in materiais:
        print("Código não encontrado!")

    elif not materiais[codigo]["disponivel"]:
        print("Material não disponível!")

    else:
        print("Material disponível!")

        if nome_usuario == "":
            nome_usuario = input("Nome do utilizador: ")
            nome_fornecedor = input("Nome do fornecedor: ")

        data_entrega = input("Data de entrega : ")
        data_devolucao = input("Data de devolução : ")

        registo = {
            "utilizador": nome_usuario,
            "fornecedor": nome_fornecedor,
            "material": materiais[codigo]["nome"],
            "codigo": codigo,
            "entrega": data_entrega,
            "devolucao": data_devolucao
        }

        registos.append(registo)

        materiais[codigo]["disponivel"] = False

        print("Empréstimo registado com sucesso!")

    continuar = input("\nDeseja emprestar outro material ? (sim/não): ").lower()

    if continuar != "sim":
        break

print("\nREGISTOS DE EMPRÉSTIMOS")

for registo in registos:
    print("\nUtilizador:", registo["utilizador"])
    print("Fornecedor:", registo["fornecedor"])
    print("Material:", registo["material"])
    print("Código:", registo["codigo"])
    print("Entrega:", registo["entrega"])
    print("Devolução:", registo["devolucao"])

print("\nFim")
