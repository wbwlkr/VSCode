# roulette très simplifier en vue de travailler ce que l'on a vu sur le cour
import random
import math


"""joueurs"""

print("Vous avez 500$")
mise = input("Saisissez une mise: ")
mise = int(mise)
init = 500 - mise
print("il vous reste:",init,)
num = input("Saisissez un numéro sur lequel miser ( entre 0 et 49): ")       
num = int(num) 
      

if num%2 ==0:
     print("votre numéro:",num," est Noire")
if num%2 != 0:
     print("Votre numéro:",num,"est Rouge")

print("Faites tournez la roulette:\n")     

"""Roulette"""
num1 = random.randrange(50)
print("Le numéro qui est sorti est le:",num1,"\n")

if num1 == num:
      print(num1,"Vous avez gagnez gros, Félicitation!\n", mise * 3,"$") 
elif num1%2 == 0:
      print(num1, "est Noire\n")
      if num%2 ==0:
            print(num,"est Noire également. Vous avez gagnez 50% de votre mise\n", mise * 0.50,"$")
      else:
            print (num,"est Rouge, vous avez perdu\n")
else:                    
      print(num1, "est Rouge\n")
      if num%2 != 0:
           print(num, "est Rouge, vous avez gagnez 50% de votre mise\n", mise * 0.50, "$")
      else:
           print(num, "est Noire, vous avez perdu\n")
     
print("Vous avez maintenant:",init,"$")              

input("Saissisez la touche Entrée pour Quitter")