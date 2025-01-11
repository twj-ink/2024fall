n = int(input())
total = 0
for _ in range(n):
    p = input()
    if p == 'Tetrahedron':
        total += 4
    elif p == 'Cube':
        total += 6
    elif p == 'Octahedron':
        total += 8
    elif p == 'Dodecahedron':
        total += 12
    elif p == 'Icosahedron':
        total += 20
print(total)


