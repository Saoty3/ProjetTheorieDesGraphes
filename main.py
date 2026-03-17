from Function import *

cst =0
while cst == 0:
    #Séléction du graphe parmi les 13 proposés
    num =None
    while num is None:
        try:
            temp = int(input("Quelle graphe entre 1 et 13 voulez vous analyser ?\n"))
            if 1<= temp <= 13:
                num = temp
            else:
                print("Ce graphe n'existe pas\n")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide\n")

    #Passage du graphe sous forme txt à la forme matriciel
    try:
        matrice = txt_to_matrice(num)
    except FileNotFoundError:
        print("Erreur : Le fichier introuvable")
        continue
    except PermissionError:
        print("Erreur : Accès refusé")
        continue

    df = pd.DataFrame(matrice)
    print("Matrice initial : \n",df)

    #Application de l'algorithme de floyd-warshall
    P, matrice = floyd_warshall(matrice)
    #Calcul de la matrice P représentant les sommets amélioré par l'algorithme
    df = pd.DataFrame(P)
    print("Matrice P des sommet qui sont modifiés\n", df)
    new_df = pd.DataFrame(matrice)
    print("\nMatrice amélioré : \n",new_df)

    #Vérification si l'utilisateur veut quitter le programme après le calcul matriciel
    cont = input("Voulez-vous continuer ? (y/n)\n")
    while cont != "y" and cont != "n":
        cont = input("Vous vous êtes trompé de réponse.\nVoulez-vous continuer ? (y/n)\n")
    if cont == "n":
        cst = 1