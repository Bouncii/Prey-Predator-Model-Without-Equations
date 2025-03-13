from random import*

# Paramètres de l'environnement
largeur = 5
longueur = 5
environnement = [[0 for j in range(largeur)] for i in range(longueur)]
nb_itérations = 10

nb_predateurs_initiale = 2
faim_predateur_initale = 5

nb_proies_initiale = 7

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
        
    def se_deplacer(self, environnement: list,tab_predateur):
        '''Fonction qui permet de déplacer une proie aléatoirement'''
        tab_direction=[(0,1),(1,0),(0,-1),(-1,0)]
        shuffle(tab_direction)
        direction = tab_direction[0]
        i=1
        while (not verification_direction_possible_bordures(self, direction, environnement) or not self.verification_direction_possible_autre_proie(direction, tab_proie) or not self.verification_direction_possible_predateur(direction,tab_predateur)) and i<=3  : 
            direction=tab_direction[i]
            i+=1


        if i==4:
            direction=(0,0)#Pas de déplacement si aucune direction trouvée

        #Déplacement de la proie
        self.x += direction[0]
        self.y += direction[1]


    def verification_direction_possible_autre_proie(self, direction:tuple, tab_proie: list):
        '''Vérifie si la proie se dirige vers une autre proie'''
        for proie in tab_proie:
            if proie.x == self.x+direction[0] and proie.y == self.y+direction[1]:
                return False
        return True
    
    def verification_direction_possible_predateur(self, direction:tuple, tab_pred: list):
        '''Vérifie si la proie se dirige vers une autre proie'''
        for pred in tab_pred:
            if pred.x == self.x+direction[0] and pred.y == self.y+direction[1]:
                return False
        return True
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
        tab_direction=[(0,1),(1,0),(0,-1),(-1,0)]
        shuffle(tab_direction)
        direction = tab_direction[0]
        i=1
        while not verification_direction_possible_bordures(self, direction, environnement):
            direction=tab_direction[i]
            i+=1
        if i==4:
            direction=(0,0)#Pas de déplacement si aucune direction trouvée

        self.verification_mange_proie(direction, tab_proie)

        #Déplacement du prédateur
        self.x += direction[0]
        self.y += direction[1]

    def verification_mange_proie(self, direction:tuple, tab_proie: list):
        '''vérifie si le prédateur mange une proie'''
        new_x=self.x+direction[0]
        new_y=self.y+direction[1]
        for proie in tab_proie[:]:  # Copie pour éviter modification en boucle
            if proie.x == new_x and proie.y == new_y:
                tab_proie.remove(proie)  # La proie est mangée
                self.décompte_faim = self.n_faim
                environnement[proie.y][proie.x]=0
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

def verification_direction_possible_bordures(self, direction: int, environnement: list):
    '''Vérifie si le déplacement est faisable par rapport aux bordures'''
    new_x=self.x+direction[0]
    new_y=self.y+direction[1]
    if new_y >= len(environnement) or new_y < 0 or new_x >= len(environnement[0]) or new_x < 0:
        return False
    return True

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

def info_proie(predateur: Predateur):
    '''Affiche les informations d'une proie'''
    print(f'Prédateur: x={predateur.x}, y={predateur.y}')
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

for i in range(nb_itérations):
    environnement = [[0 for j in range(largeur)] for i in range(longueur)]

    for proie in tab_proie:
        proie.se_deplacer(environnement,tab_predateur)
        proie.afficher()

    for predateur in tab_predateur[:]:  # Copie par mesure de securité
        predateur.se_deplacer(environnement, tab_proie)
        if predateur.décompte_faim == 0: #On retire de l'environneeent les prédateurs morts de faim

            tab_predateur.remove(predateur)
        if predateur in tab_predateur:
            info_predateur(predateur)
            predateur.afficher()



        

    afficher_environnement(environnement)


# TODO Vérifier si tout les tanleaux entrée de fonctions sont bien nécéssaires
# TODO Remplacer newx et newy par un tuple
#Dédoublement pour apparition 
