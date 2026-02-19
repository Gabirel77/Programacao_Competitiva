def fracoes():
    N = int(input())    
    fibo = [0,1]
    maior=0
    if N ==0:
        print(1)
    else:
        for i in range(N+2):
            if i !=0 and i!=1:
                fibo.append(fibo[i-2] + fibo[i-1])
            maior=i
        print(fibo[maior])


fracoes()