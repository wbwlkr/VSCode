from random import randrange
#Présentation de l'IA et première interaction, demande de prénom
print("Bonjour, mon nom est Joseph_2020.11.14.01, Je suis une future Intelligence Artificiel développer dans le but de répondre au Test de Turing.\n")

while True:
      repos = str()
      Nom = str()
      while True:
            Nom = input("Quel est votre prénom? : \n")
            try: 
                  Nom == str(Nom)      
            except:
                  print("Je n'ai pas compris, veuillez répéter svp\n")
                  continue
            if Nom == "Merde" or Nom == "merde" or Nom == "rien" or Nom == "Rien" or "Je n'ai pas de nom" or Nom == "je n'ai pas de nom" or Nom == "Pute" or Nom == "PD" or Nom == "pd" or Nom == "Pd":
                  print("Ce n'est pas très gentil de ne pas me prendre au serieux, mais je vous laisse une chance de me dire votre vrai prénom et non pas {}\n".format(Nom))
                  continue
            elif Nom == "Joseph" or Nom == "joseph" or Nom == "jo" or Nom == "Jo":
                  print("Comme moi je suis content de discuter avec vous\n")
                  break
                  #Fin de présentation, début du dialogue
      print("Maintenant que les présentation sont faites mon chère utilisateur {}, nous pouvons passer aux choses serieuses.".format(Nom))
      
      #repons1 = str()
      #while True:
            #reponse1 = input("Comment puis-je vous aidez? ")
            #if reponse1 == "Que dois-je faire aujourd'hui?" or reponse1 == "que dois-je faire aujourd'hui?" or reponse1 == "aujourd'hui" or reponse1 == "aujourd'hui?":
      