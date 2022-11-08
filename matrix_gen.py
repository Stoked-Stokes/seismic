import numpy as np
import random

def arraysToMatrix(vertices, edges):
    numVertices = len(vertices)
    matrix = [[0 for x in range(numVertices)] for y in range (numVertices)]

    for i in edges:
        x, y = i
        if(y < x):
            matrix[y][x]=1
        else:
            matrix[x][y]=1
    
    return matrix

def printMatrix(matrix):
    numVertices = len(matrix)
    for i in range(numVertices):
        for j in range(numVertices):
            print(matrix[i][j],end = " ")
        print()

def matrixToArrays(matrix):

    edges = []
    vertices = [i for i in range(len(matrix))]
    
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (matrix[row][col] == 1 & row != col):
                if(row > col):
                    tup = (col, row)
                else:
                    tup = (row, col)

                if tup not in edges:
                    edges.append(tup)

def randomMatrix(numVertices):
    matrix = np.array([[0 for x in range(numVertices)] for y in range (numVertices)])

    for j in range (numVertices):
        for i in range (numVertices):
            if (i == j):
                break
            matrix[i][j] = random.randint(0,1)
    return matrix