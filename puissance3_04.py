

from random import choice


def mot(nbr_lettre):

    lettres = ["a","h","k","o","n","s","t"]
    word = ""

    for i in range(nbr_lettre):
        word = word + choice(lettres)
    return word

nbr_lettre = int(input("- Combien de lettres ? : "))

print(mot(nbr_lettre))







