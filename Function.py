def txt_to_matrice(num):
    with open (f"Graphe{num}.txt","r") as f:
        n = int(f.readline())
        m = int(f.readline())

        matrice = [[float('inf') for j in range(m)] for i in range(n)]

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