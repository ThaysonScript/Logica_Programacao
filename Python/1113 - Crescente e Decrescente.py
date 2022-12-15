while True:
    vals = map(int, input().split())
    n1, n2 = vals

    if n1 > n2:
        print('Decrescente')
    elif n2 > n1:
        print('Crescente') 
    elif n1 == n2:
        break
