a, b = input().split()
simple = []
vyvod = set()
for i in range(int(b)):
    x = 0
    for g in range(1, int(b)):
        if i % g == 0:
            x += 1
    if x < 3:
        simple.append(i)
del simple[0]
ind = False
for i in range(int(a) + 1, int(b)):
    for el in simple:
        mnoj = []
        x = i // el
        if i % el == 0 and x in simple and x != simple[simple.index(el)]:
            vyvod.add(i)
            ind = True
        elif i % el == 0:
            mnoj.append(el)
            y = 0
            while x > 20 and y < 10:
                y += 1
                for el_2 in simple:
                    g = x // el_2
                    if x % el_2 == 0 and g in simple and g != simple[simple.index(el_2)] and el_2 not in mnoj:
                        vyvod.add(i)
                        ind = True
                        x //= el_2
                        mnoj.append(el_2)
                        break
if ind:
    vyvod = list(vyvod)
    vyvod.sort()
    print(*vyvod)
else:
    print('NO')
