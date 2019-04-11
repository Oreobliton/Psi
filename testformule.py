from random import *

decrochage_base = uniform(0.95, 1.05)
difficulte = 1
filiere = uniform(0.95, 1)
note = ((randint(0, 20))/20)
influence = uniform(0.10, 1)
pb_perso = uniform(0.90, 1.10)

def decrochage(decrochage_base, difficulte, filiere, note, influence, pb_perso):
    pourcent_decrochage = (decrochage_base * difficulte * filiere * pb_perso * influence * note)
    j = 0
    for k in range(1000000):
        i = randint(0, 100)/100
        if (i <= pourcent_decrochage):
           
            j+= 1
    print(j/1000000)


decrochage(decrochage_base, difficulte, filiere, note, influence, pb_perso)
