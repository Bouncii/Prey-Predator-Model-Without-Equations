import numpy as np
import matplotlib.pyplot as plt
import csv

def extraction_donnees_csv(fichier):
    population_predateurs = []
    population_proies = []

    with open(fichier, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)  # Ignorer l'en-tête

        for ligne in reader:
            if len(ligne) >= 2:  # Vérification pour éviter les lignes vides
                population_predateurs.append(int(ligne[0]))
                population_proies.append(int(ligne[1]))


    return population_predateurs, population_proies


fichier_csv = "predateurs_30/proies_100/faim_3/nrpred_4/nrproie_10/pred_30_proies_100_faim_3_nrpred_4_nrproie_10.csv"
preds, proies = extraction_donnees_csv(fichier_csv)


preds = np.array(preds)
proies = np.array(proies)


iterations = np.arange(len(proies))


print("Population prédateurs :", preds)
print()
print("Population proies :", proies)


plt.plot(iterations, proies, label="Proies", color="green")
plt.plot(iterations, preds, label="Prédateurs", color="red")
plt.xlabel("Itérations")
plt.ylabel("Population")
plt.title("Évolution des populations dans l'environnement")
plt.legend()
plt.show()