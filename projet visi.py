# 0 = case vide
# 1 = proie
# 2 = prédateur

from random import randint

# Création de l'environnement

largeur=5
longueur=5
environnement=[[0 for j in range(largeur)] for i in range(longueur) ]



######################################################################################
# Création de la classe Proie

class Proie:
    def __init__(self,x:int,y:int,nrproie:int):
        self.x=x
        self.y=y
        self.vie=True
        self.nrproie=nrproie
        self.reproduction=0


######################################################################################
# Création de la classe Prédateur

class Predateur:
    def __init__(self,x:int,y:int,n_faim:int):
        self.x=x
        self.y=y
        self.vie=True
        self.reproduction=0
        self.n_faim=n_faim
        self.décompte_faim=n_faim
    
    def afficher(self):
        '''Fonction qui permet d'afficher le predateur sur la grille'''
        environnement[self.y][self.x]=2

    def se_deplacer(self,environnement:list,tab_proie:list):
        '''Fonction qui permet au prédateur de se déplacer'''

        direction=randint(0,3) # On choisit une direction aléatoire
        while verification_direction_bordures(self,direction,environnement)==False: # On change de direction si le prédateur est sur les bordures et s'apprète à sortir
            direction=randint(0,3)

        
            


        self.mort_faim()


        if direction==0: # On calcul les nouvelles coordonnées du prédateur
            new_x=self.x
            new_y=self.y+1
        elif direction==1:
            new_x=self.x
            new_y=self.y-1

        elif direction==2:
            new_x=self.x+1
            new_y=self.y
        else:
            new_x=self.x-1
            new_y=self.y
    
        self.verification_mange_proie(environnement,new_x,new_y) # On vérifie si le prédateur mange une proie lors de son futut déplacement



        self.x=new_x
        self.y=new_y


    def verification_mange_proie(self,environnement:list,new_x:int,new_y:int):
        '''Fonction qui permet au prédateur de manger une proie'''

        if environnement[new_y][new_x]==1:
            self.décompte_faim=self.n_faim

        else:
            self.décompte_faim-=1


    def mort_faim(self):
        '''Fonction qui permet de savoir si le prédateur est mort'''
        if self.décompte_faim==0:
            self.vie=False


######################################################################################
# Fonctions utiles

def afficher_environnement(environnement:list):
    '''Fonction qui permet d'afficher l'environnement'''
    print()
    for ligne in environnement:
        print(ligne)
    print()

def verification_direction_bordures(self,direction:int,environnement:list):
    '''Fonction qui permet de vérifier si le prédateur ne sort pas des bordures'''
    if direction==0:
        if self.y+1>len(environnement)-1:
            return False
        else:
            return True
    elif direction==1:
        if self.y-1<0:
            return False
        else:
            return True
    elif direction==2:
        if self.x+1>len(environnement[0])-1:
            return False
        else:
            return True
    else:
        if self.x-1<0:
            return False
        else:
            return True



######################################################################################
# Programme principal
tab_proie = [Proie(randint(0, largeur - 1), randint(0, longueur - 1), 5) for i in range(0)]
tab_pred = [Predateur(randint(0, largeur - 1), randint(0, longueur - 1), 5) for i in range(1)]

for i in range(6):
    environnement = [[0 for j in range(largeur)] for i in range(longueur)]

    # On fait une copie de tab_pred pour éviter les erreurs de modification pendant l'itération
    copie_tab_pred = tab_pred[:]

    for pred in copie_tab_pred:
        pred.se_deplacer(environnement, tab_proie)
        
        if not pred.vie: 
            tab_pred.remove(pred)
        else:
            pred.afficher()
            print(pred.x, pred.y, pred.décompte_faim)

    afficher_environnement(environnement)