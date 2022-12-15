lista = []
soma = 0
while True:
    vals = map(int, input().split())
    n1, n2 = vals

    if n1 > -1 and n2 > -1:
        lista.append(n1)
        lista.append(n2)
        lista.sort()

        if n1 != 0 and n2 != 0:
            for x in range(lista[0], lista[1] + 1):
                print(f'{x}', end= ' ')
            for x in range(lista[0], lista[1] + 1):
                soma = soma + x
            print(f'Sum={soma}')
            lista.clear()
            soma = 0

    if n1 <= 0 or n2 <= 0:
        break
