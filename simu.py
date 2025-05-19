from projet_visi import execution_environnement  

def simu():
    

    fichier=open("input.txt","r")
    largeur=int(fichier.readline())
    longueur=int(fichier.readline())
    nb_iterations=int(fichier.readline())


    nb_predateurs_initiale=int(fichier.readline())
    nb_proies_initiale=int(fichier.readline())
    faim_predateur_initiale=int(fichier.readline())
    nrpred=int(fichier.readline())
    nrproie=int(fichier.readline())
    fichier.close()


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


simu()