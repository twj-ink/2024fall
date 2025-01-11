t = int(input())

s = 1 + 2 + 3

while True:
    while t % s != 0:
        s += 1
        '''
        if s > t**0.5:
            t = s
            break
        '''

    found = False
    for x in range(1, s):
        for y in range(x + 1, s):
            if y == x:
                continue
            for z in range(y + 1, s):
                if s - x - y != z:
                    continue
                if z == y or z == x:
                    continue
                # print(f'{x},{y},{z}')
                found = True
                break

            if found:
                break
        if found:
            break

    if found:
        break

print(t // s)