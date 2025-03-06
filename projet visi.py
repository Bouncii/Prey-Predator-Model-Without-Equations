from random import randint

# Paramètres de l'environnement
largeur = 5
longueur = 5
environnement = [[0 for j in range(largeur)] for i in range(longueur)]
nb_itérations = 10

nb_predateurs_initiale = 1
faim_predateur_initale=5

nb_proies_initiale = 3

nrpred=30
nrproie=30
######################################################################################
# Création de la classe Proie

class Proie:
    def __init__(self, x: int, y: int, nrproie: int):
        self.x = x
        self.y = y
        self.nrproie = nrproie
        self.reproduction = 0

    def afficher(self):
        '''Affiche la proie sur la grille'''
        environnement[self.y][self.x] = 1
        
    def se_deplacer(self, environnement: list):
        direction = randint(0, 3)
        if direction == 0:
            new_x = self.x
            new_y = self.y + 1
        elif direction == 1:
            new_x = self.x
            new_y = self.y - 1
        elif direction == 2:
            new_x = self.x + 1
            new_y = self.y
        else:
            new_x = self.x - 1
            new_y = self.y

        while not verification_direction_bordures(self, direction, environnement) and not self.verification_direction_autre_proie(new_x, new_y, tab_proie): 
            direction = randint(0, 3)

            if direction == 0:
                new_x = self.x
                new_y = self.y + 1
            elif direction == 1:
                new_x = self.x
                new_y = self.y - 1
            elif direction == 2:
                new_x = self.x + 1
                new_y = self.y
            else:
                new_x = self.x - 1
                new_y = self.y


        #Déplacement de la proie
        self.x = new_x 
        self.y = new_y


    def verification_direction_autre_proie(self, new_x: int, new_y: int, tab_proie: list):
        '''Vérifie si la proie se dirige vers une autre proie'''
        for proie in tab_proie:
            if proie.x == new_x and proie.y == new_y:
                return True
        return False
    
######################################################################################
# Création de la classe Prédateur

class Predateur:
    def __init__(self, x: int, y: int, n_faim: int, nrpred:int):
        self.x = x
        self.y = y
        self.nrpred=nrpred
        self.reproduction = 0
        self.n_faim = n_faim
        self.décompte_faim = n_faim

    def afficher(self):
        '''Affiche le prédateur sur la grille'''
        environnement[self.y][self.x] = 2

    def se_deplacer(self, environnement: list, tab_proie: list):
        '''Déplacement du prédateur'''

        direction = randint(0, 3)
        while not verification_direction_bordures(self, direction, environnement):
            direction = randint(0, 3)

        if direction == 0:
            new_x = self.x
            new_y = self.y + 1
        elif direction == 1:
            new_x = self.x
            new_y = self.y - 1
        elif direction == 2:
            new_x = self.x + 1
            new_y = self.y
        else:
            new_x = self.x - 1
            new_y = self.y

        self.verification_mange_proie(new_x, new_y, tab_proie)

        #Déplacement du prédateur
        self.x = new_x 
        self.y = new_y

    def verification_mange_proie(self, new_x: int, new_y: int, tab_proie: list):
        '''vérifie si le prédateur mange une proie'''
        for proie in tab_proie[:]:  # Copie pour éviter modification en boucle
            if proie.x == new_x and proie.y == new_y:
                tab_proie.remove(proie)  # La proie est mangée
                self.décompte_faim = self.n_faim

        # Réduction de la faim si rien n'a été mangé
        self.décompte_faim -= 1  

######################################################################################
# Fonctions utiles

def afficher_environnement(environnement: list):
    '''Affichage de la grille'''
    print()
    for ligne in environnement:
        print(ligne)
    print()

def verification_direction_bordures(self, direction: int, environnement: list):
    '''Vérifie si l'entité se dirige vers une bordure'''
    if direction == 0 and self.y + 1 >= len(environnement):
        return False
    elif direction == 1 and self.y - 1 < 0:
        return False
    elif direction == 2 and self.x + 1 >= len(environnement[0]):
        return False
    elif direction == 3 and self.x - 1 < 0:
        return False
    return True

def trouve_coordonnees_vide(environnement: list):
    '''Trouve des coordonnées vides dans l'environnement'''
    x = randint(0, len(environnement[0]) - 1)
    y = randint(0, len(environnement) - 1)
    while environnement[y][x] != 0:
        x = randint(0, len(environnement[0]) - 1)
        y = randint(0, len(environnement) - 1)
    return (x, y)


def info_predateur(predateur: Predateur):
    '''Affiche les informations des prédateurs'''
    print(f'Prédateur: x={predateur.x}, y={predateur.y}, décompte_faim={predateur.décompte_faim}')

######################################################################################
# Programme principal

tab_proie = [Proie(trouve_coordonnees_vide(environnement)[0], trouve_coordonnees_vide(environnement)[1], nrproie) for i in range(nb_proies_initiale)]
tab_predateur = [Predateur(trouve_coordonnees_vide(environnement)[0], trouve_coordonnees_vide(environnement)[1], faim_predateur_initale,nrpred) for i in range(nb_predateurs_initiale)]

for i in range(nb_itérations):
    environnement = [[0 for j in range(largeur)] for i in range(longueur)]

    for predateur in tab_predateur[:]:  # Copie par mesure de securité
        predateur.se_deplacer(environnement, tab_proie)
        if predateur.décompte_faim == 0: #On retire de l'environneeent les prédateurs morts de faim
            tab_predateur.remove(pred)


    # Affichage des entités restantes
    for proie in tab_proie:
        proie.se_deplacer(environnement)

    for proie in tab_proie:
        proie.afficher()

    for pred in tab_predateur:
        info_predateur(predateur) ### info pour Test
        pred.afficher()


        

    afficher_environnement(environnement)


# TODO Vérifier si tout les tanleaux entrée de fonctions sont bien nécéssaires
# TODO Remplacer newx et newy par un tuple
#Dédoublement pour apparition 
