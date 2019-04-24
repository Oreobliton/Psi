# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import matplotlib.pyplot as plt
from testformuleSPEEDUP import *

liste = simulation2()[1]

print(len(liste))

for i in liste:
    plt.plot(i)

strdepart = "taux de départ : "
strfin = "taux à la fin : "
strDecro1 = "Eleves en cours à la fin : "


plt.savefig('Textless.png', dpi=300)
plt.ylabel('Taux decroch')
plt.xlabel('Semaines')
axes = plt.gca()
axes.set_xlim([0,45])
axes.set_ylim([0,160])
plt.savefig('withText.png', dpi=500)
plt.show()

