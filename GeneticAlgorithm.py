import numpy as np
import random

#Convert vertices and edges to matrix and vice versa ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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



#Random matrix generation ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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




#Graph connections - looking for pathway /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def in_graph(G, a, b):
    if G.shape[0] < (a+1) or G.shape[0] < (b+1):
        print("Vertex index out of bounds!")
        return False
    return True

def connected(G, a, b):
    # If an upper triangular matrix is passed in as an argument, uncomment the following line of code:
    # G = G + np.transpose(G)
    if not in_graph(G, a, b):
        return
    if a == b:
        # print('Yes')
        return True
    matrix_len = G.shape[0]
    if G[a, b] == 1:
        # print('Yes')
        return True
    G_1 = G
    for i in range(1, matrix_len):
        G_1 = np.matmul(G_1, G)
        if G_1[a, b] == 1:
            # print('Yes')
            return True
    # print('No')
    return False

def same_comp(G, s, a):
    """Returns true if a is in the same connected components as vertices in set s. 
    G is the graph, s is a set, a is a vertex"""
    # If an upper triangular matrix is passed in as an argument, uncomment the following line of code:
    # G = G + np.transpose(G)
    for x in s:
        if connected(G, a, x):
            return True
        return False

def conn_comps(G):
    # If an upper triangular matrix is passed in as an argument, uncomment the following line of code:
    # G = G + np.transpose(G)
    matrix_len = G.shape[0]
    comps = []
    if len(comps) == 0:
        x = {0}
        comps.append(x)
    for i in range(1, matrix_len):
        t = 0
        for aset in comps:
            if same_comp(G, aset, i):
                aset.add(i)
                t = 1
                break
        if t == 0:
            y = {i}
            comps.append(y)
    return len(comps)


if __name__ == "__main__":
    G = np.array([[0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0]])
    a = 0
    b = 4
    # connected(G, a, b)
    print(conn_comps(G))

    # m = 2
    # n = 2
    # connected(G, m, n)

    H = np.array([0])
    x = 0
    y = 0
    # connected(H, x, y)
    print(conn_comps(H))

    # j = 1
    # k = 1
    # connected(H, j, k)
    M = np.array([[0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 0]])
    print(conn_comps(M))