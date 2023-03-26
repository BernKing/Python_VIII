def maior_cidade(ficheiro):
    cidade_max = ''
    pop_max = 0
    for line in ficheiro:
        cidade_temp, pop_temp = line.strip().split(',')

        pop_temp = int(pop_temp)

        if pop_temp > pop_max:
            cidade_max = cidade_temp
            pop_max = pop_temp

    print("Cidade: ", cidade_max, "\nPop: ", pop_max)


user1 = input("Ficheiro:")

ficheiro1 = user1 + ".txt"

with open(ficheiro1, "r") as ficheiro:
    maior_cidade(ficheiro)

