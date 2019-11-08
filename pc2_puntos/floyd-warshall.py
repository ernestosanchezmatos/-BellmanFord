import numpy as np

numVertices = 5
grafo = [[0, 5,15, 7, np.inf],
         [np.inf,0, np.inf,3,10],
         [np.inf, np.inf, 0,np.inf,1],
         [np.inf,np.inf, 2,0,8],
         [np.inf,np.inf,np.inf,np.inf,0]]
     

def floydWarshall(grafo):
    for k in range(numVertices):
        for i in range(numVertices):
            for j in range(numVertices):
                if grafo[i][j] > grafo[i][k] + grafo[k][j]:
                    grafo[i][j] = grafo[i][k] + grafo[k][j]

    for i in range(numVertices):
        if (grafo[i][i] < 0):
            print("Hay ciclo negativo")

floydWarshall(grafo)
print("Esta es una matrix de costo optimizado")

print(grafo[0])
print(grafo[1])
print(grafo[2])
print(grafo[3])
print(grafo[4])

