from random import *

global difficulte
difficulte = 1

###############################################################################Partie classe, et fonction d'initialisation de la classe groupe

class Groupe():
    def __init__(self):
        self.decrochage_base = randint(95,105)/100 #est exprimé en pourcentage
        self.filiere = filiere()
        self.influence = influence()
        self.pb_perso = pb_perso()
        self.note = True
        self.taux_Decrochage = 0
                
        
    def decrochage(self):
        taux_decrochage = (self.decrochage_base * difficulte * self.filiere * self.pb_perso * self.influence * self.note)
        print(taux_decrochage)
        print(self.taux_Decrochage)
        self.taux_Decrochage = taux_decrochage
        
    
    def variationDurantLannee(self): #permet de faire evoluer le taux tout au long de l'année.
        taux = randint(80,120)/100
        self.taux_Decrochage +=  self.decrochage()
        self.taux_Decrochage *=  taux
    
    def debug(self): #sert juste à afficher les valeurs pour comprendre où ça plante
        print(self.decrochage_base)
        print(self.filiere)
        print(self.influence)
        print(self.pb_perso)
        print(self.note)
        print(self.taux_Decrochage)
        print("-------------- fin de la semaine \n")

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
    return(aleatoire/100000)
        
######################################################################################################################### Debut de la partie simul°

# def testMoy():
    # promo = list()
    # for i in range(20):
        # promo.append(Groupe())
    # compteur_decroch = 0
    # print(promo[0].debug() )
    # for i in range(20):
        # compteur_decroch += decrochage(promo[i])
    # print(compteur_decroch/20)#Pour l'instant on est 0.25 trop haut !!!
        
def simulation():
    promo = list()
    for i in range(20):
        promo.append(Groupe())
    semaine = 0
    while semaine < 3:
        for i in range(len(promo)):
            promo[i].variationDurantLannee()
            print(promo[i].debug())
        semaine+=1 
  

#Péartie test  
"""PENSER AU RECROCHAGE"""
#testMoy()
#promo = Groupe()
#decrochage(promo)
#influence()
simulation()
