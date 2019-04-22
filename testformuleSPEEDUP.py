from random import *

global difficulte
difficulte = 1

###############################################################################Partie classe, et fonction d'initialisation de la classe groupe

class Groupe():
    def __init__(self):
        
        """Partie ou on définit les valeurs d'un groupe lors de son initialisation"""
        self.decrochage_base = randint(15,30)/100 #est exprimé en pourcentage
        self.filiere = filiere()
        self.influence = influence() 
        self.pb_perso = pb_perso()
        
        """ La on va définir des variables qui peuvent evoluer au cours le simulation"""
        self.taux_Decrochage = 0.0
        self.decrocher = False
        self.note = True
        self.cpt = 0 # compte les semaines consécutives durant lesquelles un étudiant n'est pas allé en cours (est réinitialisée si il va en cours)
        self.chance_pas_revenir=randint(20,40)/100 #correspond à l'état mental des étudiants
    def decrochage(self):
        taux_decrochage = (self.decrochage_base * difficulte * self.filiere * self.pb_perso * self.influence * self.note)
        return taux_decrochage
    
    def variationDurantLannee(self): #permet de faire evoluer le taux tout au long de l'année.
        taux = randint(70,120)/100
        self.taux_Decrochage +=  self.decrochage()
        self.taux_Decrochage *=  taux
    
    def debug(self): #sert juste à afficher les valeurs pour comprendre où ça plante
        print(self.decrochage_base)
        # print(self.filiere)
        # print(self.influence)
        # print(self.pb_perso)
        # print(self.note)
        print("Le taux de décrochage du groupe est de : ",self.taux_Decrochage*100,"%")
        print("L'élève a il décroché ? : ",self.decrocher)
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
        
def vaEnCours(groupe):
    chance_Decrocher = randint(0,100)/100
    if chance_Decrocher >= groupe.taux_Decrochage:
        return True #signifie qu'il VA en cours
    return False #signifie qu'il ne VA PLUS en cours

def compteurDecrochage(groupe):
    if vaEnCours(groupe) == True:     #Réinitialisation du compteur
        groupe.cpt = 0
    
    if vaEnCours(groupe) == False:    #Il est pas allé en cours : incrémentation du compteur
        groupe.cpt += 1

    if groupe.cpt > 2:
        groupe.decrocher = True       #ça fait trois semaine qu'il est pas venu : il est en décrochage.

def raccrochage(groupe):
    chance_Raccrochage = randint(0,100) / 100
    if chance_Raccrochage >= groupe.chance_pas_revenir:    #signifie que le groupe REVIENT en cours
        groupe.decrocher = False
        groupe.taux_Decrochage = randint(10,30)/100
    else:                                               #signifie que le groupe n'est pas revenu : ses chances de revenir baissent (même si on les augmente, la formule fait qu'on diminue la chance de revenir)
        groupe.chance_pas_revenir += 5
######################################################################################################################### Debut de la partie simul°

def testMoy(nbGroupe):
    promo = list()
    for i in range(nbGroupe):
        promo.append(Groupe())
    compteur_decroch = 0
    print(promo[0].debug() )
    for i in range(nbGroupe-1):
        promo[i].variationDurantLannee()
        compteur_decroch += promo[i].taux_Decrochage
    print("La moyenne de décrochage pour un groupe de ",nbGroupe," groupes est de :",compteur_decroch/nbGroupe)#Pour l'instant on est 0.25 trop haut !!!
        
def simulation():
    promo = list()
    for i in range(20):
        promo.append(Groupe())
    semaine = 0
    while semaine < 10:
        for i in range(len(promo)-1): #-1 parce que sinon on dépasse la taille de la promo et c'est pas fou
                
            if promo[i].decrocher == False: #Cas où le groupe n'a pas décroché, on vérifie qu'il aille en cours cette semaine
                promo[i].variationDurantLannee()
                compteurDecrochage(promo[i])
                
            elif promo[i].decrocher == True:
                raccrochage(promo[i])
        print("\n")
        promo[0].debug()
            
        semaine+=1 
#Péartie test  
"""PENSER AU RECROCHAGE"""
#testMoy(10000)
#promo = Groupe()
#decrochage(promo)
#influence()
simulation()
