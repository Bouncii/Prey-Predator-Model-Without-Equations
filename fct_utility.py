from Predateur_module import Predateur
from Proie_module import Proie
from random import randint

def afficher_environnement(environnement: list):
    '''Affichage de la grille'''
    print()
    for ligne in environnement:
        print(ligne)
    print()


def trouve_coordonnees_vide(environnement: list, tab_proie: list, tab_predateur: list):
    '''Trouve une case qui est vide  (elle n'est occupée ni par une proie ni par un prédateur)'''
    cases_vides = []
    for y in range(len(environnement)):
        for x in range(len(environnement[0])):
            # Vérifie si la case est libre
            est_occupe = False
            for proie in tab_proie:
                if proie.x == x and proie.y == y:
                    est_occupe = True
            
            for predateur in tab_predateur:
                if predateur.x == x and predateur.y == y:
                    est_occupe = True
            
            if not est_occupe:
                cases_vides.append((x, y))
    
    if len(cases_vides) > 0:
        index = randint(0, len(cases_vides) - 1)
        return cases_vides[index]
    return None  # Retourne None si aucune case vide n'est trouvée


def info_predateur(predateur: Predateur):
    '''Affiche les informations d'un predateur'''
    print(f'Prédateur: x={predateur.x}, y={predateur.y}, décompte_faim={predateur.décompte_faim}')

def info_proie(proie: Proie):
    '''Affiche les informations d'une proie'''
    print(f'Proie: x={proie.x}, y={proie.y}')

def est_iteration_apparition(i,nr_entite):
    """Verifie si l'iteration actuelle i est une itération ou une entite se reproduit """
    return i % nr_entite == 0