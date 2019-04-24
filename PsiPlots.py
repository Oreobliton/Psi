# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import matplotlib.pyplot as plt
from testformuleSPEEDUP import *

liste = simulation4 ()

print(len(liste))
print(liste)
plt.plot(liste)

strdepart = "taux de départ : "
strfin = "taux à la fin : "
strDecro1 = "Eleves en cours à la fin : "


plt.savefig('Textless.png', dpi=300)
plt.ylabel('Moyenne taux decroch')
plt.xlabel('Semaines')
axes = plt.gca()
axes.set_xlim([0,45])
axes.set_ylim([0,160])
plt.savefig('withText.png', dpi=500)
plt.show()

