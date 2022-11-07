import numpy as np
#Starting with 5 vertices
vertices = [0,1,2,3,4]
edges = [(0,1),(0,3),(0,4),(1,2),(2,3), (1,0)]

def arraysToMatrix(vertices, edges):
    
    numVertices = len(vertices)
    
    #print(numVertices)

    #matrix = [numVertices][numVertices]
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
    
    #vertices = []
    edges = []
    #print(len(matrix))
    #for i in range(len(matrix)):

       # vertices[i] = i

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

    
    """
    for i in range(len(matrix)):
        print(vertices[i],end = " ")
    print()

    for tup in edges:
        print("(" , tup[0], ",", tup[1], ")", sep = "", end = "")
    """
       

#matrix = arraysToMatrix(vertices, edges)
matrix2 = arraysToMatrix(vertices, edges)
matrix3 = [[1,1,1], [1,1,1], [1,1,1]]
#printMatrix(matrix3)
matrixToArrays(matrix3)