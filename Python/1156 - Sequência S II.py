s = 0
denom = 1

for cont in range(1, 39, 2):
    s = s + (cont / denom)
    denom = denom * 2
print(f'{s:.2f}')
