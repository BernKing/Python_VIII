def conversao(texto):
    with open("OsMaias2", "w") as novo:
        for char in texto.read():
            if char.islower():
                char1 = char.upper()
                novo.write(char1)
            elif char.isupper():
                char2 = char.lower()
                novo.write(char2)
            else:
                novo.write(char)


user = str(input("Ficheiro: "))
ficheiro = user + ".txt"

with open(ficheiro, "r", encoding="utf-8-sig") as texto:
    conversao(texto)
