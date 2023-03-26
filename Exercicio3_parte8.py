def conversao(texto):
    with open("OsMaias3", "w") as novo:
        for char in texto.read():
            if char in "aeiouAEIOUáàéÁÀÈÉ":
                novo.write("*")
            else:
                novo.write(char)


user = str(input("Ficheiro: "))
ficheiro = user + ".txt"

with open(ficheiro, "r", encoding="utf-8-sig") as texto:
    conversao(texto)
