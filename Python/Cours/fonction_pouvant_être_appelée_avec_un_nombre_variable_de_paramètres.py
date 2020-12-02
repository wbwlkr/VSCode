>>> def fonction_inconnue(*parametres):
...     """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
...     
...     print("J'ai reçu : {}.".format(parametres))
... 
>>> fonction_inconnue() # On appelle la fonction sans paramètre
J'ai reçu : ().
>>> fonction_inconnue(33)
J'ai reçu : (33,).
>>> fonction_inconnue('a', 'e', 'f')
J'ai reçu : ('a', 'e', 'f').
>>> var = 3.5
>>> fonction_inconnue(var, [4], "...")
J'ai reçu : (3.5, [4], '...').
>>>