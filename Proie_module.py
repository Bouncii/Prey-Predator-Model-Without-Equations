from random import shuffle

class Proie:
    def __init__(self, x: int, y: int, nrproie: int):
        self.x = x
        self.y = y
        self.nrproie = nrproie
        self.reproduction = 0

    def afficher(self,environnement):
        '''Affiche la proie sur la grille'''
        environnement[self.y][self.x] = 1
        
    def se_deplacer(self,environnement: list,tab_proie,tab_predateur):
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
        '''Vérifie si la proie ne se dirige pas vers une autre proie'''
        for proie in tab_proie:
            if proie.x == self.x+direction[0] and proie.y == self.y+direction[1]:
                return False
        return True
    
    def verification_direction_possible_predateur(self, direction:tuple, tab_pred: list):
        '''Vérifie si la proie ne se dirige pas vers un predateur'''
        for pred in tab_pred:
            if pred.x == self.x+direction[0] and pred.y == self.y+direction[1]:
                return False
        return True
    

def verification_direction_possible_bordures(self, direction: int, environnement: list):
    '''Vérifie si le déplacement est faisable par rapport aux bordures'''
    new_x=self.x+direction[0]
    new_y=self.y+direction[1]
    if new_y >= len(environnement) or new_y < 0 or new_x >= len(environnement[0]) or new_x < 0:
        return False
    return True