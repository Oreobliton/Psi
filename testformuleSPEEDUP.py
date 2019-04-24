from random import *

global difficulte
difficulte =1 

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
        self.chance_pas_revenir=randint(20,50)/100 #correspond à l'état mental des étudiants
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
        print("Les chances de pas revenir : ",self.chance_pas_revenir)
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
        groupe.chance_pas_revenir = randint(20,50)/100
    else:                                               #signifie que le groupe n'est pas revenu : ses chances de revenir baissent (même si on les augmente, la formule fait qu'on diminue la chance de revenir)
        groupe.chance_pas_revenir += 15/100
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
    evolution = list() #cette liste contiendra les données concernant l'évolution des groupes au long de l'année (utile pour les graphiques)
    for i in range(20):
        promo.append(Groupe())
    semaine = 0
    while semaine < 10:
        for i in range(len(promo)-1): #-1 parce que sinon on dépasse la taille de la promo et c'est pas fou
                
            if promo[i].decrocher == False: #Cas où le groupe n'a pas décroché, on vérifie qu'il aille en cours cette semaine
                promo[i].variationDurantLannee() 
                compteurDecrochage(promo[i])
                evolution.append(promo[i].taux_Decrochage *100)

            elif promo[i].decrocher == True:
                raccrochage(promo[i])

        # print("\n")                   #partie utile pour le débug
        # promo[0].debug()    
        semaine+=1 
    return evolution

def moyenne(promo,tick,variable): #pour avoir les infos de la promo à un tick donné (
    if tick == variable:
        cpt = 0
        sommeMental=0
        sommeTauxD =0
        for i in promo:
            sommeMental += i.chance_pas_revenir
            sommeTauxD  += i.taux_Decrochage
            if i.decrocher == True:
                cpt += 1 
        return (sommeTauxD/len(promo), len(promo)-cpt)
    else:
        pass

def TroisCourbes(promo):
    somme = 0
    for i in promo:
        if i.decroche == False:
            somme += 1
    return somme

            


def simulation2():
    promo = list()
    gigaliste = list() #contiendra TOUTES LES SOUS LISTES evolution
    moy = list()
    for i in range(10):
        promo.append(Groupe())
    
    for groupe in promo:
        semaine = 1
        evolution = list() #cette liste contiendra les données concernant l'évolution des groupes au long de l'année (utile pour les graphiques)
        while semaine <= 41:
             
            if groupe.decrocher == False: #Cas où le groupe n'a pas décroché, on vérifie qu'il aille en cours cette semaine
                groupe.variationDurantLannee() 
                compteurDecrochage(groupe)
                evolution.append(groupe.taux_Decrochage *100)

            elif groupe.decrocher == True:
                raccrochage(groupe)
                evolution.append(groupe.taux_Decrochage *100)

            gigaliste.append(evolution)
            moy = moyenne(promo,42,semaine)
            semaine+=1
    print(moy) 
    return (moy,gigaliste)



def simulation3(): 
    promo = list()
    evolution = list() #cette liste contiendra les données concernant l'évolution des groupes au long de l'année (utile pour les graphiques)
    for i in range(20):
        promo.append(Groupe())
    semaine = 0
    while semaine < 42:
        addition = 0
        for i in range(len(promo)-1): #-1 parce que sinon on dépasse la taille de la promo et c'est pas fou
            if promo[i].decrocher == False: #Cas où le groupe n'a pas décroché, on vérifie qu'il aille en cours cette semaine
                promo[i].variationDurantLannee() 
                compteurDecrochage(promo[i])
                addition += (promo[i].taux_Decrochage *100)
            elif promo[i].decrocher == True:
                raccrochage(promo[i])
        evolution.append(addition/20)
        semaine+=1 
    return evolution

def simulation4(): #EN COURS DE TRAVAIL
    promo = list()
    evolution = list() #cette liste contiendra les données concernant l'évolution des groupes au long de l'année (utile pour les graphiques)
    for i in range(20):
        promo.append(Groupe())
    semaine = 0
    while semaine < 42:
        dehors = 0
        for i in promo:
            print(i.decrocher)#-1 parce que sinon on dépasse la taille de la promo et c'est pas fou
            if i.decrocher: #Cas où le groupe n'a pas décroché, on vérifie qu'il aille en cours cette semaine
                dehors += 1
        evolution.append(dehors)
        semaine+=1
    return evolution

############################################################################################################################  Partie test  
"""PENSER AU RECROCHAGE"""
#testMoy(10000)
#promo = Groupe()
#decrochage(promo)
#influence()
#simulation()
# o = Groupe()
# o.decrocher = True
# print("-------------------test Avant : ")
# o.debug()
# raccrochage(o)
# print("-------------------test Après : ")
# o.debug()
