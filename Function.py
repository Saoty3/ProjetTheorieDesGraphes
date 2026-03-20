from pathlib import Path
import math


INF = float("inf")


def format_value(x):
    if x == INF:
        return "∞"
    return str(x)


def afficher_matrice(matrice, nom="Matrice"):
    n = len(matrice)
    largeur = 6

    print(f"\n{nom}")
    print(" " * largeur + "".join(f"{j:>{largeur}}" for j in range(n)))

    for i in range(n):
        ligne = f"{i:>{largeur}}"
        for j in range(n):
            ligne += f"{format_value(matrice[i][j]):>{largeur}}"
        print(ligne)


def lire_graphe(num):
    chemin = Path(__file__).resolve().parent / f"Graphe_{num}.txt"

    if not chemin.exists():
        raise FileNotFoundError(f"Fichier introuvable : {chemin}")

    with open(chemin, "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())

        matrice = [[INF for _ in range(n)] for _ in range(n)]

        # distance d'un sommet à lui-même = 0
        for i in range(n):
            matrice[i][i] = 0

        nb_lus = 0
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            u, v, w = map(int, ligne.split())
            matrice[u][v] = w
            nb_lus += 1

        if nb_lus != m:
            print(
                f"Attention : le fichier annonce {m} arcs, "
                f"mais {nb_lus} arcs ont été lus."
            )

    return matrice


def floyd_warshall(matrice_initiale):
    n = len(matrice_initiale)

    # copie profonde
    dist = [ligne[:] for ligne in matrice_initiale]

    # matrice des prédécesseurs
    pred = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != INF:
                pred[i][j] = i

    historiques_L = []
    historiques_P = []

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    nouvelle_distance = dist[i][k] + dist[k][j]
                    if nouvelle_distance < dist[i][j]:
                        dist[i][j] = nouvelle_distance
                        pred[i][j] = pred[k][j]

        historiques_L.append([ligne[:] for ligne in dist])
        historiques_P.append([ligne[:] for ligne in pred])

    return dist, pred, historiques_L, historiques_P


def contient_circuit_absorbant(dist):
    n = len(dist)
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False


def reconstruire_chemin(pred, depart, arrivee):
    if depart == arrivee:
        return [depart]

    if pred[depart][arrivee] is None:
        return None

    chemin = [arrivee]
    courant = arrivee

    while courant != depart:
        courant = pred[depart][courant]
        if courant is None:
            return None
        chemin.append(courant)

    chemin.reverse()
    return chemin


def afficher_tous_les_chemins(dist, pred):
    n = len(dist)
    print("\nChemins minimaux :")
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            chemin = reconstruire_chemin(pred, i, j)
            if chemin is None or dist[i][j] == INF:
                print(f"De {i} à {j} : aucun chemin")
            else:
                texte_chemin = " -> ".join(map(str, chemin))
                print(f"De {i} à {j} : coût minimal = {dist[i][j]}, chemin = {texte_chemin}")


def afficher_matrice_predecesseurs(pred, nom="Matrice P"):
    n = len(pred)
    largeur = 6

    print(f"\n{nom}")
    print(" " * largeur + "".join(f"{j:>{largeur}}" for j in range(n)))

    for i in range(n):
        ligne = f"{i:>{largeur}}"
        for j in range(n):
            val = "-" if pred[i][j] is None else str(pred[i][j])
            ligne += f"{val:>{largeur}}"
        print(ligne)
