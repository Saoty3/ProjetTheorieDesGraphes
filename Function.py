import pandas as pd


def txt_to_matrice(num):
    with open (f"Graphe_{num}.txt","r") as f:
        # Récolte des premières informations sur la matrice
        n = int(f.readline())   #Nombre de bases de 0 n (lignes)
        m = int(f.readline())   #Nombre d'associations dans le graphe

        #Création de la matrice avec "inf" comme valeur de base
        matrice = [[float('inf') for j in range(n)] for i in range(n)]

        #Mise en place des différentes valeurs de la matrice
        for lines in f:
            u,v,w = map(int, lines.split())
            matrice[u][v] = w


    return matrice

def floyd_warshall(dist):
    n = len(dist)

    P = [[None for j in range(n)]for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

                    P[i][j] = k
        print(f"\nMatrice L pour k = {k}")
        print(pd.DataFrame(dist))
    return P, dist

def accessible(matrice, start):
    visited = set()
    stack = [start]

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            for v in range (len(matrice)):
                if matrice[u][v] != float('inf'):
                    stack.append(v)
    return visited


def detect_cycle(matrice):
    access = {}

    # construire les accessibles pour chaque sommet
    for i in range(len(matrice)):
        access[i] = accessible(matrice, i)

    # vérifier les cycles
    for i in range(len(matrice)):
        for j in access[i]:
            if i != j and i in access[j]:
                print("Ce graphe contient un cycle")
                return True

    print("Pas de cycle")
    return False