def estojo():
    N = int (input())
    menor =100000
    indice = 0
    cont = 0
    for i in range(N):
        lista = list(map(int,input().split()))
        for j in range(N):
            if menor>lista[j]:
                menor = lista[j]
                indice = j
                cont=i
    if indice==cont and cont==0:
        print(0)
    elif indice<cont:
        print(3)
    elif indice>cont:
        print(1)
    else:
        print(2)

estojo()