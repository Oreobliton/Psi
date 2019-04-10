from random import * 
#L'idée c'est vraiment de mettre un zeste d'aléatoire pour éviter que l'expérience ne soit trop déterministe !

difficult = 1 #on va dire que c'est un multiplicateur(non entierentre 1 et 2)
def fil():
    a = randint(0,100)
    if a > 80:
        return False
    return True

class Etudiant:
    def __init__(self):
        self.tauxDecroch = randint(0,20) #definit le taux de decrochage initial
        self.enCours = True #definit si l'eleve est en cours ou s'il a decroche 
        self.filiere = fil() 
        self.examen = bool #definit si l'eleve a reussit ou rate ses examens (c'est notes)                
def creerPromo(etu): #fait une promo de etu etudiants
    promo = list()
    while etu > 0:
        groupe = list()
        etuDansGroupe = randint(3,7) #Cree des groupes de tailles variable entre 3 et 7
        for i in range(etuDansGroupe): 
            groupe.append(Etudiant()) #Ajoute i etudiants (avec son taux de décrochage) dans un groupe
        promo.append(groupe) #Ajoute le groupe d'etudiant dans toute la promo
        etu -= etuDansGroupe
    return promo

def stats(promo): #modifie les valeurs selon les membres d'un groupe 
    Lres = list()
    for i in promo:
        somme = 0
        for j in i:
            somme += j.tauxDecroch
        Lres.append((somme,len(i),somme/len(i)))
    print(Lres)       


a = creerPromo(50)
for i in a:
    for j in i:
        print(j.tauxDecroch, j.enCours)
etudiantsEncours(a)
stats(a)
