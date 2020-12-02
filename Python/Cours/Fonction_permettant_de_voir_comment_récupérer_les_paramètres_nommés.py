 def fonction_inconnue(**parametres_nommes):
     """Fonction permettant de voir comment récupérer les paramètres nommés
     dans un dictionnaire"""
     
     
     print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))
 
fonction_inconnue() # Aucun paramètre
J ai reçu en paramètres nommés : {}
 fonction_inconnue(p=4, j=8)
 
J ai reçu en paramètres nommés : {'p': 4, 'j': 8}
