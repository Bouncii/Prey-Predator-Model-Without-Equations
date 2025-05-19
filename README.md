# Prey Predator Model Without Equations

## Purpose
The goal of this project is to make a simulated prey and predator environment and analyze the result for various parameters. (we want to obtain the same results as [Lotka–Volterra](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations))

## 📘​ Context
This project was made for the laboratory visit project at uni.
You can see the page that i made about the project [here](http://os-vps418.infomaniak.ch:1250/mediawiki/index.php/Mod%C3%A8le_proie-pr%C3%A9dateur_sans_%C3%A9quations).

## 🚀​ Usage

Download the source code using `git clone` or download as zip file.

To run the simulation, you just need to head to the [main file](projet_visi.py), modify the parameters that you want for your simulation and then run the program !

The parameters : 
- largeur = width
- longueur = height
- nb_itérations = the number of simulation iterations
- nb_predateurs_initiale = the initial number of predators
- faim_predateur_initale = the number of iterations a predator takes to die if it fails to eat prey
- nb_proies_initiale = the initial number of preys
- nrpred = the number of iterations it takes for predators to reproduce
- nrproie = the number of iterations it takes for preys to reproduce

When your simulation is finished, you can now extract the data [here](extraction_csv.py) by replacing the csv file name line 22. (ex : fichier_csv = "pred_10_proies_50_faim_3_nrpred_4_nrproie_2.csv")

## ⚙️​ Technical Aspects
I made this using mainly python and a little bit of bash.
As you can see there is two class for each entities ([prey](Proie_module.py) and [predator](Predateur_module.py)) that interact on a grill present in the [main file](projet_visi.py) that run the simulation in its entirety.
[modele.sh](modele.sh) is here to help you to store the result of the simulations if you want to make a lot.

✨​Enjoy !✨​

