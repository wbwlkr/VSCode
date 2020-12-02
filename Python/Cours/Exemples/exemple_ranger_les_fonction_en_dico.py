def fete():    
    print("C'est la fête.")


def oiseau():
    print("Fais comme l'oiseau...")

fonctions = {}
fonctions["fete"] = fete # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]
<function oiseau at 0x00BA5198>

fonctions["oiseau"]() # on essaye de l'appeler
Fais comme l'oiseau...
