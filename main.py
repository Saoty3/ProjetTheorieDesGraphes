from Function import (
    lire_graphe,
    floyd_warshall,
    contient_circuit_absorbant,
    reconstruire_chemin,
    afficher_matrice,
    afficher_matrice_predecesseurs,
    afficher_tous_les_chemins,
)

NB_GRAPHES = 14


def traiter_graphe(num):
    print("\n" + "=" * 60)
    print(f"Analyse du graphe {num}")
    print("=" * 60)

    matrice = lire_graphe(num)
    afficher_matrice(matrice, "Matrice initiale")

    dist, pred, historiques_L, historiques_P = floyd_warshall(matrice)

    for k in range(len(historiques_L)):
        afficher_matrice(historiques_L[k], f"Matrice L après k = {k}")
        afficher_matrice_predecesseurs(historiques_P[k], f"Matrice P après k = {k}")

    afficher_matrice(dist, "Matrice finale des distances minimales")
    afficher_matrice_predecesseurs(pred, "Matrice finale P")

    if contient_circuit_absorbant(dist):
        print("\nLe graphe contient au moins un circuit absorbant.")
        print("Dans ce cas, certains plus courts chemins ne sont pas définis.")
        return

    print("\nLe graphe ne contient pas de circuit absorbant.")

    while True:
        choix = input("\nVoulez-vous afficher un chemin minimal précis ? (o/n) : ").strip().lower()
        if choix == "n":
            break
        if choix != "o":
            print("Réponse invalide.")
            continue

        try:
            depart = int(input("Sommet de départ : "))
            arrivee = int(input("Sommet d'arrivée : "))
        except ValueError:
            print("Veuillez entrer des entiers.")
            continue

        if not (0 <= depart < len(dist) and 0 <= arrivee < len(dist)):
            print("Sommet invalide.")
            continue

        chemin = reconstruire_chemin(pred, depart, arrivee)
        if chemin is None or dist[depart][arrivee] == float("inf"):
            print(f"Aucun chemin de {depart} à {arrivee}.")
        else:
            print(
                f"Chemin minimal de {depart} à {arrivee} : "
                + " -> ".join(map(str, chemin))
            )
            print(f"Coût minimal : {dist[depart][arrivee]}")

    choix_tous = input("\nVoulez-vous afficher tous les chemins minimaux ? (o/n) : ").strip().lower()
    if choix_tous == "o":
        afficher_tous_les_chemins(dist, pred)


def main():
    while True:
        try:
            num = int(input(f"\nQuel graphe entre 1 et {NB_GRAPHES} voulez-vous analyser ? "))
        except ValueError:
            print("Veuillez entrer un entier.")
            continue

        if not (1 <= num <= NB_GRAPHES):
            print(f"Ce graphe n'existe pas. Choisissez un nombre entre 1 et {NB_GRAPHES}.")
            continue

        try:
            traiter_graphe(num)
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Erreur pendant le traitement du graphe {num} : {e}")

        recommencer = input("\nVoulez-vous analyser un autre graphe ? (o/n) : ").strip().lower()
        if recommencer != "o":
            print("Fin du programme.")
            break


if __name__ == "__main__":
    main()
