# -*-coding:utf-8 -*
annee = input("Saisissez une année:")
try:
       annee = int(annee)
       assert annee > 0
except ValueError:
      print("Vous n'avez pas saissi un nombre") 
except AssertionError:
       print("Vous devez saisir une annee supérieur a 0.")       
       
if annee % 400 == 0:
      print(" l'annee est bissextille")
elif annee % 100 == 0:
      print(" l'annee est bissextille")
elif annee % 4 == 0:
      print("l'annee est bissextille") 
else:           
      print(" l'annee n'est pas bissextille")
# On met le programme en pause pour éviter qu'il ne se referme (Windows)

input("appuyer sur entrée pour fermer le programme")