import os
from projet_visi import execution_environnement  

def arborescence():
    
    largeur = 20
    longueur = 20
    nb_iterations = 200

    
    valeurs_predateurs = [10, 30, 50]
    valeurs_proies = [50, 100, 150]
    valeurs_faim = [3, 5]
    valeurs_nrpred = [4, 6]
    valeurs_nrproie = [2, 3]

    
    dossier_racine = "data"
    os.makedirs(dossier_racine, exist_ok=True)

    # Arborescence en 5 niveaux, chaque niveau correspondant à un paramètre
    total_combinaisons = len(valeurs_predateurs) * len(valeurs_proies) * len(valeurs_faim) * len(valeurs_nrpred) * len(valeurs_nrproie)
    combinaison_courante = 0 

    for nb_predateurs_initiale in valeurs_predateurs:
        dossier_pred = os.path.join(dossier_racine, f"nb_predateurs_{nb_predateurs_initiale}")
        os.makedirs(dossier_pred, exist_ok=True)


        for nb_proies_initiale in valeurs_proies:
            dossier_proie = os.path.join(dossier_pred, f"nb_proies_{nb_proies_initiale}")
            os.makedirs(dossier_proie, exist_ok=True)


            for faim_predateur_initiale in valeurs_faim:
                dossier_faim = os.path.join(dossier_proie, f"faim_{faim_predateur_initiale}")
                os.makedirs(dossier_faim, exist_ok=True)


                for nrpred in valeurs_nrpred:
                    dossier_nrpred = os.path.join(dossier_faim, f"nrpred_{nrpred}")
                    os.makedirs(dossier_nrpred, exist_ok=True)


                    for nrproie in valeurs_nrproie:
                        dossier_final = os.path.join(dossier_nrpred, f"nrproie_{nrproie}")
                        os.makedirs(dossier_final, exist_ok=True)


                        # Sauvegarde du répertoire de travail courant
                        dir_courant = os.getcwd()
                        # On change de dossier pour que le CSV généré soit créé dans ce dossier
                        os.chdir(dossier_final)

                        # Affichage du chemin pour suivi
                        combinaison_courante += 1
                        print(f"Lancement de la simulation {combinaison_courante}/{total_combinaisons}: {dossier_final}")

                        
                        execution_environnement(
                            largeur,
                            longueur,
                            nb_iterations,
                            nb_predateurs_initiale,
                            faim_predateur_initiale,
                            nb_proies_initiale,
                            nrpred,
                            nrproie
                        )

                        # Retour au répertoire initial
                        os.chdir(dir_courant)

    print("Toutes les simulations ont été exécutées avec succès.")

arborescence()