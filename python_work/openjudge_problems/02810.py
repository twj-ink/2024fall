n=int(input())
cube={} #用字典把bcd的所有结果保存，减少嵌套
for b in range(2,n+1):
    for c in range(b,n+1):
        for d in range(c,n+1):
            result=b**3+c**3+d**3
            if result not in cube:
                cube[result]=[]
                cube[result].append((b,c,d))
for a in range(2,n+1):
    if a**3 in cube:
        for b,c,d in cube[a**3]:
            print(f'Cube = {a}, Triple = ({b},{c},{d})')
