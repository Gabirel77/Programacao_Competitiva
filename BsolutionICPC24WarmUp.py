def verifica_altura():
    qtd_brinq = int(input())
    altura_carl = int(input())
    altura_brin = 0
    contagem = 0

    altura_brin = input()
    lista = list(map(int, altura_brin.split()))
    
    for j in range(len(lista)): 
        if lista[j]<=altura_carl:
            contagem+=1
    print(contagem)

verifica_altura()