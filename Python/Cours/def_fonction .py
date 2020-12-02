# -*-coding:utf-8 -*
"""module multipli contenant la fonction table"""
def table(nb, max):
   i = 0
   while i < max:
       print( i + 1, "*", nb,"=", ( i + 1 )*nb )
       i += 1
       
nb = input("Saisissez un nombre : ")
nb = int(nb)

max = input("saisissez un maximum : ")
max = int(max)

table(nb, max)

input("appuyez sur entrer pour fermer le programme")