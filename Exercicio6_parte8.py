def ler_dados():
    pessoas = []
    telefone = None
    while telefone != 0:
        dicionario = {"nomes": '', "telefones": 0}
        nome = input("Nome: ")
        telefone = int(input("Telefone: "))
        if telefone != 0:
            dicionario.update({"nomes": nome, "telefones": telefone})
            pessoas.append(dicionario)
        else:
            introduzir_ficheiro(pessoas)


def introduzir_ficheiro(pessoas):
    with open("Pessoas.txt", "w") as pessoazinhas:
        for i in range(len(pessoas)):
            pessoazinhas.write(pessoas[i]["nomes"])
            pessoazinhas.write("\n")
            pessoazinhas.write(str(pessoas[i]["telefones"]) + "\n")



ler_dados()
