import numpy as np

def estojo():
    valori=0
    valorj=0
    menor=1000000
    N = int (input())
    matriz = np.zeros((N,N))
    for i in range(N):
        lista = list(map(int,input().split()))
        for j in range(N):
            matriz[i][j]= lista[j]
            if matriz[i][j]< menor:
                menor=matriz[i][j]
                valori=i
                valorj=j
    if valori==valorj and valorj==0:
        print(0)
    elif valorj<valori:
        print(3)
    elif valorj>valori:
        print(1)
    else:
        print(2)

estojo()