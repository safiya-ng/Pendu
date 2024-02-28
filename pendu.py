import random
import os

with open("tous_les_mots.txt","r") as liste_mot:
  liste_mot = liste_mot.readlines() 
  mot1 = "".join(liste_mot)
  mot1 = mot1.split("\n")


def difficulte(liste):
    print("Voici les échelles de difficulté du jeu:\n\n - Niveau 1 : La longueur est comprise entre 9 lettres et plus\n\n - Niveau 2 : La longueur des mots est comprise entre 5 lettres et 8 lettres\n\n - Niveau 3 : La longeur des mots est comprise entre 1 lettre et 4 lettres ")
  
    diff=0
    listemot=[]
    while (diff != 1) and (diff!=2) and (diff!=3):
      diff = int(input("\nVeuillez choisir l'un des niveau.(1 pour niveau 1, 2 pour niveau 2, 3 pour niveau 3) \n\n  Niveau :  "))
      if diff == 1:
        listemot= [i for i in liste if len(i)>= 9]
      elif diff == 2: 
        listemot = [i for i in liste if len(i)>=5 and len(i)<9]
      elif diff == 3:
        listemot = [i for i in liste if len(i) <5]
    return listemot 

def choisir_mot():
    return list(random.choice(difficulte(mot1)))


def efface_ecran():
  if os.name == 'nt':
    os.systeme('cls')
  else:
    os.system('clear')

def dessinPendu(nb):
    tab=[
    """""",
    """
    


    
    

    ==============
    """
    ,
    """
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    
    return tab[nb]
      

def gagner(liste, compteur, mot):
  if "_ " not in liste:
    print("Vous avez gagné !")
    print()
    return True
  elif compteur == 9:
    print(f"\n Vous avez perdu,\n le mot était {mot}")
  else:
    return False


def lettre_valide ():
  valide = [chr(c) for c in range (65,91)] + [chr(c) for c in range (97,123)]
  lettre = input("Entrer une lettre: ")
  while lettre not in valide:
    print("La lettre entrée n'est pas valide")
    lettre = input("Entrer une autre lettre: ")
  if lettre in valide:
    lettre = lettre.upper()
  return lettre 


def lettre_entrees(lettre_valide):
  l = []
  l.append(lettre_valide)
  l = ",".join(l)
  return f"Vous avez déjà entré: {l} "


def jouer():
  jouer = ""
  while (jouer != "oui") or (jouer != "non"):
    jouer= input("\nVoulez-vous jouer au pendu ? (oui pour jouer. non pour ne pas jouer ) \n\n")
    if jouer == "oui":
      efface_ecran()
      print("Bonne chance ;)\n\n")
      return True
    elif jouer == "non":
      efface_ecran()
      print("Bonne continuation !!")
      return False


def jeu():
  play=jouer()
  while play == True:
    mot_cache = choisir_mot()
    mot_a_trouver = "".join(mot_cache)
    liste_lettre = []
    liste_cache=["_ " for i in range(len(mot_cache))]
    efface_ecran()
    print(" ".join(liste_cache))
    compteur_erreur=0
    while gagner(liste_cache, compteur_erreur, mot_a_trouver ) == False:
      lettre= lettre_valide()
      if lettre in mot_cache:
        for i in range(mot_cache.count(lettre)):
          z = mot_cache.index(lettre)
          mot_cache[z] = '*'
          liste_cache[z]=(lettre+" ")
        mot_c = "".join(liste_cache)
        efface_ecran()
        print(dessinPendu(compteur_erreur))
        print(mot_c)
      elif lettre not in mot_cache:
        if lettre not in liste_lettre :
          compteur_erreur+=1
          mot_c = "".join(liste_cache)
          efface_ecran()
          print(dessinPendu(compteur_erreur))
          print(mot_c) 
        elif lettre in liste_lettre:
          efface_ecran()
          print(dessinPendu(compteur_erreur))
          print(mot_c) 
          print(lettre_entrees(lettre))
      if lettre not in liste_lettre:
        liste_lettre.append(lettre)
      chaine_lettre = "".join(liste_lettre)
      print(f"lettres rentrées précedemment: {chaine_lettre}")
      print(f"Il vous reste {9-compteur_erreur} chances avant d'être pendu")
    play=jouer()
    if play=="non":
      return play
      



print(jeu())