from random import randint

# Création de l'environnement
largeur = 5
longueur = 5
environnement = [[0 for j in range(largeur)] for i in range(longueur)]

######################################################################################
# Création de la classe Proie

class Proie:
    def __init__(self, x: int, y: int, nrproie: int):
        self.x = x
        self.y = y
        self.vie = True
        self.nrproie = nrproie
        self.reproduction = 0

######################################################################################
# Création de la classe Prédateur

class Predateur:
    def __init__(self, x: int, y: int, n_faim: int):
        self.x = x
        self.y = y
        self.vie = True
        self.reproduction = 0
        self.n_faim = n_faim
        self.décompte_faim = n_faim

    def afficher(self):
        '''Afficher le prédateur sur la grille uniquement s'il est vivant'''
        if self.vie:
            environnement[self.y][self.x] = 2

    def se_deplacer(self, environnement: list, tab_proie: list):
        '''Le prédateur se déplace et meurt immédiatement s'il a faim'''
        if not self.vie:
            return

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

        self.verification_mange_proie(environnement, new_x, new_y, tab_proie)

        if self.décompte_faim == 0: # Mort de faim
            self.vie = False  

        if self.vie:  # Ne pas déplacer s'il est mort
            self.x = new_x
            self.y = new_y

    def verification_mange_proie(self, environnement: list, new_x: int, new_y: int, tab_proie: list):
        '''Le prédateur mange une proie et réinitialise sa faim'''
        for proie in tab_proie[:]:  # Copie pour éviter modification en boucle
            if proie.x == new_x and proie.y == new_y:
                tab_proie.remove(proie)  # La proie est mangée
                self.décompte_faim = self.n_faim

        self.décompte_faim -= 1  # Réduction de la faim si rien n'a été mangé

######################################################################################
# Fonctions utiles

def afficher_environnement(environnement: list):
    '''Affichage de la grille'''
    print()
    for ligne in environnement:
        print(ligne)
    print()

def verification_direction_bordures(self, direction: int, environnement: list):
    '''Empêche de sortir des bordures'''
    if direction == 0 and self.y + 1 >= len(environnement):
        return False
    elif direction == 1 and self.y - 1 < 0:
        return False
    elif direction == 2 and self.x + 1 >= len(environnement[0]):
        return False
    elif direction == 3 and self.x - 1 < 0:
        return False
    return True

######################################################################################
# Programme principal

tab_proie = [Proie(randint(0, largeur - 1), randint(0, longueur - 1), i) for i in range(3)]
tab_pred = [Predateur(randint(0, largeur - 1), randint(0, longueur - 1), 5) for _ in range(1)]

for i in range(6):
    environnement = [[0 for j in range(largeur)] for i in range(longueur)]

    for pred in tab_pred[:]:  # Copie par mesure de securité
        pred.se_deplacer(environnement, tab_proie)

    # Suppression immédiate des prédateurs morts
    tab_pred = [pred for pred in tab_pred if pred.vie]

    # Affichage des entités restantes
    for proie in tab_proie:
        environnement[proie.y][proie.x] = 1
    for pred in tab_pred:
        pred.afficher()
<<<<<<< HEAD
    # print(pred.x, pred.y, pred.décompte_faim) check predateurs
    # print(tab_pred)
    afficher_environnement(environnement)
=======
        print(pred.x, pred.y, pred.décompte_faim) 
    # print(tab_pred)
    afficher_environnement(environnement)


# TODO Changer la manière dont son opéré les morts et organiser tout ça
#Quand prédateurs meurent de faim, les supprimer du tableau sans le self.vie
#Dédoublement pour apparition 
>>>>>>> master
