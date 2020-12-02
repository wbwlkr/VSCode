#exemple dans l'interpréteur Python d'ouverture de fichier

>>> mon_fichier = open("fichier.txt", "r")
>>> mon_fichier
<_io.TextIOWrapper name='fichier.txt' encoding='cp1252'>
>>> type(mon_fichier)
<class '_io.TextIOWrapper'>
>>>

#lire l'intégralité du fichier

>>> mon_fichier = open("fichier.txt", "r")
>>> contenu = mon_fichier.read()
>>> print(contenu)
C'est le contenu du fichier. Spectaculaire non ?
>>> mon_fichier.close()
>>>

#enregistrer des modifs
import pickle
>>> with open('donnees', 'wb') as fichier:
...     mon_pickler = pickle.Pickler(fichier)
...     # enregistrement ...
... 
>>>

>>> score = {
...   "joueur 1":    5,
...   "joueur 2":   35,
...   "joueur 3":   20,
...   "joueur 4":    2,
>>> }
>>> with open('donnees', 'wb') as fichier:
...     mon_pickler = pickle.Pickler(fichier)
...     mon_pickler.dump(score)
... 
>>>

#Récupérer nos objets enregistrés

>>> with open('donnees', 'rb') as fichier:
...     mon_depickler = pickle.Unpickler(fichier)
...     # Lecture des objets contenus dans le fichier...
... 
>>>