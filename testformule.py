from random import *

global difficulte
difficulte = 1

class Groupe():
    def __init__(self):
        self.decrochage_base = randint(95,105)/100 #est exprimé en pourcentage
        self.filiere = filiere()
        self.influence = influence()
        self.pb_perso = pb_perso()
        self.note = True
    
    def debug(self): #sert juste à afficher les valeurs pour comprendre où ça plante
        print(self.decrochage_base)
        print(self.filiere)
        print(self.influence)
        print(self.pb_perso)
        print(self.note)

def filiere(): #définit la filière de l'étudiant (True ou False) 
    aleatoire = randint(0,100) 
    if aleatoire <= 10: 
        return 1.05 
    else : 
        return 0.95 
    
def pb_perso():
    aleatoire = randint(0,10000)
    if (aleatoire <= 500):
        return 1.1
    elif (aleatoire >= 9500):
        return 0.9
    else:
        return 1

def influence():
    aleatoire = randint(0,80000)
    #print((0.6)+(aleatoire/100000)) 
    return(aleatoire/100000)

# def influence(): #Pour tester la validité d'influence
    # moy = 0
    # for i in range(1000000):
        # moy += influence2()
    # print(moy/1000000)

def decrochage(groupe):
    pourcent_decrochage = (groupe.decrochage_base * difficulte *groupe.filiere *groupe.pb_perso *groupe.influence *groupe.note)
    return pourcent_decrochage
    #j = 0
    # for k in range(1000000):
        # i = randint(0, 100)/100
        # if (i <= pourcent_decrochage):
           
            # j+= 1
    # print(j/1000000)

def testMoy():
    promo = list()
    for i in range(20):
        promo.append(Groupe())
    compteur_decroch = 0
    print(promo[0].debug() )
    for i in range(20):
        compteur_decroch += decrochage(promo[i])
    print(compteur_decroch/20)#Pour l'instant on est 0.25 trop haut !!!
#Partie test  
"""PENSER AU RECROCHAGE"""
#testMoy()
#promo = Groupe()
#decrochage(promo)
#influence()
