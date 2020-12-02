# --coding:utf-8 -
from random import randrange

ins = int()
ins1 = str()

print("Voici le générateur d'insulte fait par ce gros con de Mathieu, allez Enjoy, ou pas bande de pute\n")
while ins != 20:
    lettre = input("Si vous voulez sortir, tappez 'q' ou tappez 'Entrer pour voir s'afficher une insulte: ")
    if lettre == "q":
        print("Va niquer ta mère si ça t'amuse pas! j'me ferme moi !\n")
        break
    ins = randrange(15)
    if ins == 0:
        ins1 = "\nNique ta mère\n"
        print(ins1.upper().center(90))
        continue
    if ins == 1:
        ins1 = "\nFils de pute\n"
        print(ins1.upper().center(90))
        continue
    if ins == 2:
        ins1 = "\nSale Pute\n "
        print(ins1.upper().center(90))
        continue
    if ins == 3:
        ins1 = "\nTon Oncle\n"
        print(ins1.upper().center(90))
        continue
    if ins == 4:
        ins1 = "\nPeigne Cul\n"
        print(ins1.upper().center(90))
        continue
    if ins == 5:
        ins1 = "\nPeigne Zizi\n"
        print(ins1.upper().center(90))
        continue
    if ins == 6:
        ins1 = "\nVa chier dans ta caisse\n"
        print(ins1.upper().center(90))
        continue
    if ins == 7:
        ins1 = "\nJe t'encule\n"
        print(ins1.upper().center(90))
        continue
    if ins == 8:
        ins1 = "\nJe me tape ta mère à l'arrière d'une Twingo\n"
        print(ins1.upper().center(90))
        continue
    if ins == 9:
        ins1 = "\nTa grand mère\n"
        print(ins1.upper().center(90))
        continue
    if ins == 10:
        ins1 =  "\nMon programmeur est une Pute, déso\n"
        print(ins1.upper().center(90))
        continue
    if ins == 11:
        ins1 =  "\nGarage à bite\n"
        print(ins1.upper().center(90))
        continue
    if ins == 12:
        ins1 =  "\nGrosse Chatte\n"
        print(ins1.upper().center(90))
        continue
    if ins == 13:
        ins1 = "\nSalope\n"
        print(ins1.upper().center(90))
        continue
    if ins == 14:
        ins1 =  "\nGobe mon énorme chibre\n"
        print(ins1.upper().center(90))
        continue                                                          
fin = input("\nAppuie sur Entre pour me fermer bordel! ")