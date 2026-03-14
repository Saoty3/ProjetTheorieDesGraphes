def txt_to_matrice(num):
    with open (f"Graphe{num}.txt","r") as f:
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

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist