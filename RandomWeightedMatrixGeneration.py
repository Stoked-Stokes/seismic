import VerticesEdgesToMatrix
import numpy as np
import random

#print(random.randint(0,1))

def randomMatrix (numVertices):
    matrix = [[0 for x in range(numVertices)] for y in range (numVertices)]
    # for i in range (numVertices):
    #     for j in range (numVertices):
    #         if(j > i):
    #             matrix[i][j] = random.randint(0,1)

    for j in range (numVertices):
        for i in range (numVertices):
            if (i == j):
                break
            matrix[i][j] = random.randint(0,1)
    return matrix
                

def printMatrix(matrix):
    numVertices = len(matrix)
    for i in range(numVertices):
        for j in range(numVertices):
            print(matrix[i][j],end = " ")
        print()
            

x = 7
m1 = randomMatrix(x)
printMatrix(m1)
print()
m2 = m1 + np.transpose(m1)
printMatrix(m2)


