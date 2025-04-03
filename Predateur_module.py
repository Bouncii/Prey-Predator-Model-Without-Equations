from random import shuffle

class Predateur:
    def __init__(self, x: int, y: int, n_faim: int, nrpred:int):
        self.x = x
        self.y = y
        self.nrpred=nrpred
        self.reproduction = 0
        self.n_faim = n_faim
        self.décompte_faim = n_faim

    def afficher(self,environnement):
        '''Affiche le prédateur sur la grille'''
        environnement[self.y][self.x] = 2

    def se_deplacer(self, environnement: list, tab_proie: list, tab_predateur:list):
        '''Déplacement du prédateur'''
        tab_direction=[(0,1),(1,0),(0,-1),(-1,0)]
        shuffle(tab_direction)
        direction = tab_direction[0]
        i=1
        while (not verification_direction_possible_bordures(self, direction, environnement) or not self.verification_direction_possible_autre_predateur(direction,tab_predateur)) and i<=3:
            direction=tab_direction[i]
            i+=1
        if i==4:
            direction=(0,0)#Pas de déplacement si aucune direction trouvée

        self.verification_mange_proie(environnement,direction, tab_proie)

        #Déplacement du prédateur
        self.x += direction[0]
        self.y += direction[1]

    def verification_direction_possible_autre_predateur(self, direction:tuple, tab_predateur: list):
        '''Vérifie si le prédateur ne se dirige pas vers un autre predateur'''
        for predateur in tab_predateur:
            if predateur.x == self.x+direction[0] and predateur.y == self.y+direction[1]:
                return False
        return True

    def verification_mange_proie(self,environnement,direction:tuple, tab_proie: list):
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



def verification_direction_possible_bordures(self, direction: int, environnement: list):
    '''Vérifie si le déplacement est faisable par rapport aux bordures'''
    new_x=self.x+direction[0]
    new_y=self.y+direction[1]
    if new_y >= len(environnement) or new_y < 0 or new_x >= len(environnement[0]) or new_x < 0:
        return False
    return True