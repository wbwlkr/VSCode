nb = input( "Saisissez un chiffre ou un nombre: ")
nb = int(nb)
i = 0

while i < 50:
     print(i + 1, "*", nb, "=", (i + 1) * nb)
     i += 1