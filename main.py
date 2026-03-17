import pandas as pd
from Function import *
#Séléction du graphe parmi les 13 proposés
num =0
while num > 13 or num < 1:
    num = int(input("Quelle graphe entre 1 et 13 voulez vous analyser ?\n"))
    if num > 13 or num < 1:
        print("Ce graphe n'existe pas choisissez un nombre entre 1 et 13\n")

#Passage du graphe sous forme txt à la forme matricielle
matrice = txt_to_matrice(num)
df = pd.DataFrame(matrice)
print("Matrice initial : \n",df)

#Application de l'algorithme de floyd-warshall
P, matrice = floyd_warshall(matrice)
#Calcul de la matrice P représentant les sommets amélioré par l'algorithme
df = pd.DataFrame(P)
print("Matrice P des sommet qui sont modifiés\n", df)
new_df = pd.DataFrame(matrice)
print("\nMatrice amélioré : \n",new_df)