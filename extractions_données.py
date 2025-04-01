import numpy as np
import matplotlib.pyplot as plt

def extraction_donnees(fichier):
    population_predateurs = []
    population_proies = []
    f = open(fichier, "r", encoding="utf-8")
    tab_num = [str(i) for i in range(10)]
    for ligne in f:
        
        elements = ligne.split()
        print(elements)


        if elements[0][0] in tab_num:
            i=0
            nb_pred=""
            while elements[0][i] in tab_num:
                nb_pred+=elements[0][i]
                i+=1
            population_predateurs.append(int(nb_pred))

            i+=1
            nb_proie=""
            while i<len(elements[0]):
                nb_proie+=elements[0][i]
                i+=1
            population_proies.append(int(nb_proie))


    return population_predateurs, population_proies



fichier_txt = "stat_environnement.txt"  
preds, proies = extraction_donnees(fichier_txt)


preds=np.array(preds)
proies=np.array(proies)

iterations=[i for i in range(len(proies))]

print("population predateurs :", preds)
print()
print("population proies :", proies)


plt.plot(iterations,proies)
plt.plot(iterations,preds)
plt.show()
