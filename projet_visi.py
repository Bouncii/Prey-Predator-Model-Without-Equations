from random import*
import csv
from Predateur_module import Predateur
from Proie_module import Proie
from fct_utility import*
# Paramètres de l'environnement
largeur = 20
longueur = 20

nb_itérations = 500

nb_predateurs_initiale = 30
faim_predateur_initale = 3

nb_proies_initiale = 100

nrpred=4
nrproie=2


def execution_environnement(largeur:int,longueur:int,nb_itérations:int,nb_predateurs_initiale:int,faim_predateur_initale:int,nb_proies_initiale:int,nrpred:int,nrproie:int):

    environnement = [[0 for j in range(largeur)] for i in range(longueur)]

    csv_file=f"pred_{nb_predateurs_initiale}_proies_{nb_proies_initiale}"
    csv_file+=f"_faim_{faim_predateur_initale}"
    csv_file+=f"_nrpred_{nrpred}_nrproie_{nrproie}.csv"
    csv_columns=["population_predateurs","population_proies"]


    ######################################################################################
    # Programme principal


    #Creation des entités
    tab_proie = []
    tab_predateur = []

    for i in range(nb_proies_initiale):
        coord = trouve_coordonnees_vide(environnement, tab_proie, tab_predateur)
        if coord != None:
            tab_proie.append(Proie(coord[0], coord[1], nrproie))

    for j in range(nb_predateurs_initiale):
        coord = trouve_coordonnees_vide(environnement, tab_proie, tab_predateur)
        if coord != None:
            tab_predateur.append(Predateur(coord[0], coord[1], faim_predateur_initale, nrpred))

    ############################

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(csv_columns)

        for i in range(1,nb_itérations):

            writer.writerow([len(tab_predateur), len(tab_proie)])

            environnement = [[0 for _ in range(largeur)] for _ in range(longueur)]

            for proie in tab_proie:
                proie.se_deplacer(environnement,tab_proie,tab_predateur)
                proie.afficher(environnement)

            
            nouveau_tab_predateurs = []
            for predateur in tab_predateur:
                predateur.se_deplacer(environnement, tab_proie, tab_predateur)
                
                if predateur.décompte_faim > 0:
                    nouveau_tab_predateurs.append(predateur)  # Garde le prédateur en vie
                    predateur.afficher(environnement)  

            tab_predateur = nouveau_tab_predateurs

        ###### reproduction ########

            if est_iteration_apparition(i,nrproie):
                for _ in range(len(tab_proie)):
                    coord = trouve_coordonnees_vide(environnement, tab_proie, tab_predateur)
                    if coord != None:
                        tab_proie.append(Proie(coord[0], coord[1], nrproie))
                for proie in tab_proie:
                    proie.afficher(environnement) # On affiche les nouvelles proies sur la grille
                # print("reproduction proies !",i)

            if est_iteration_apparition(i,nrpred):
                for i in range(len(tab_predateur)):
                    coord=(randint(0,largeur-1),randint(0,longueur-1))
                    tab_predateur.append(Predateur(coord[0], coord[1], faim_predateur_initale, nrpred))
                    for proie in tab_proie:
                        if proie.x == tab_predateur[i].x and proie.y == tab_predateur[i].y:
                            tab_proie.remove(proie)

                for predateur in tab_predateur:
                    predateur.afficher(environnement) # On affiche les nouveaux prédateurs sur la grille
                # print("reproduction predateurs !",i)

    ###### fin reproduction ########

        # afficher_environnement(environnement)

    print("les proies sont au nombre de:",len(tab_proie),"à la fin de la simulation")
    print("les predateurs sont au nombre de:",len(tab_predateur),"à la fin de la simulation")
