from random import *




def pb_perso():
    aleatoire = randint(0,10000)
    if (aleatoire <= 500):
        print(1.1)
        return 1.1
    elif (aleatoire >= 9500):
        print(0.9)
        return 0.9
    else:
        print(1)
        return 1


decrochage_base = uniform(0.95, 1.05)
difficulte = 1
filiere = uniform(0.95, 1)
note = ((randint(0, 20))/20)
influence = uniform(0.10, 1)
pb_perso1 = pb_perso()

def decrochage(decrochage_base, difficulte, filiere, note, influence, pb_perso1):
    pourcent_decrochage = (decrochage_base * difficulte * filiere * pb_perso1 * influence * note)
    j = 0
    for k in range(1000000):
        i = randint(0, 100)/100
        if (i <= pourcent_decrochage):
           
            j+= 1
    print(j/1000000)


decrochage(decrochage_base, difficulte, filiere, note, influence, pb_perso1)
