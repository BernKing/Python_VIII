def contar_linhas(file):
    i = 0
    for line in file:
        i += 1
    return print("Linhas:", i)


def contar_vogais(file):
    n = 0
    for char in file.read():
        if char in "aeiou":
            n += 1
    return print("Vogais:", n)


def contar_consoantes(file):
    n = 0
    for char in file.read():
        if char not in "aeiou":
            n += 1
    return print("Consoantes:", n)


def contar_caracter(file, a):

    n = 0
    for char in file.read():
        if char.lower() == a:
            n += 1

    return print("caracter:", n)


user = str(input("Ficheiro: "))
ficheiro = user + ".txt"

caracter = input("Caracter:")

with open(ficheiro, "r", encoding="utf-8-sig") as texto:
    contar_linhas(texto)
    texto.seek(0)
    contar_vogais(texto)
    texto.seek(0)
    contar_consoantes(texto)
    texto.seek(0)
    contar_caracter(texto, caracter)

# ficheiro.close()
