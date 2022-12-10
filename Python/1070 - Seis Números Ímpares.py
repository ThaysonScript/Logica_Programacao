val = int(input())
listaImpar = []

if val % 2 == 1:
    listaImpar.append(val)
    print(val)

while True:
    val += 1
    if val % 2 == 1:
        listaImpar.append(val)
        print(val)
        if len(listaImpar) == 6:
            listaImpar.clear()
            break
