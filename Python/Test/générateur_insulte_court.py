# --coding:utf-8 -
from random import randrange

t_insultes = [
    "Nique ta mère",
    "Fils de pute",
    "Sale Pute ",
    "Ton Oncle",
    "Peigne Cul",
    "Peigne Zizi",
    "Va chier dans ta caisse",
    "Je t'encule",
    "Je me tape ta mère à l'arrière d'une Twingo",
    "Ta grand mère",
    "Mon programmeur est une Pute, déso",
    "Garage à bite",
    "Grosse Chatte",
    "Salope",
    "Gobe mon énorme chibre",
]

print("Voici le générateur d'insulte fait par ce gros con de Mathieu, allez Enjoy, ou pas bande de pute\n")
while True:
    lettre = input("Si vous voulez sortir, tappez 'q' ou tappez 'Entrer pour voir s'afficher une insulte: ")
    if lettre == "q":
        print("Va niquer ta mère si ça t'amuse pas! j'me ferme moi !\n")
        break
    index_insulte_max = len(t_insultes) - 1
    index_insulte_random = randrange(index_insulte_max)
    insulte = t_insultes[index_insulte_random]
    print(str("\n" + insulte + "\n").upper().center(50))
    continue
fin = input("\nAppuie sur Entre pour me fermer bordel! ")