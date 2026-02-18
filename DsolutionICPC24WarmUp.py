def revigorante():
    lista = list(map(int, input().split()))
    D_inicial = lista[0]
    C_atividades = lista[1]
    R_atividades = lista[2]
    total_atividades=R_atividades

    listaC = []
    listaR = []
    for i in range(C_atividades):
        listaC.append(int(input()))
    for i in range(R_atividades):
        listaR.append(int(input()))
        D_inicial+=listaR[i]
    menor = 1000000;
    nova_lista=[]
    for i in range(len(listaC)):
        for j in range (len(listaC)):
            if menor > listaC[j]:
                menor=listaC[j]
        nova_lista.append(menor)
    
    for k in range(len(listaC)):
        if D_inicial - listaC[k] > 0:
            D_inicial -= listaC[k]
            total_atividades+=1
        else:
            break
    print(total_atividades)

revigorante()