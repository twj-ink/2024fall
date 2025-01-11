s='ABCDEFGHIJKL'
#while True:
#    try:
n=int(input())
for _ in range(n):
    abc=[]
    for _ in range(3):
        a,b,c=input().split()
        abc.append((a,b,c))
    for i in range(12):
        #all((在左边显示up)，(在右边显示down)，(不在显示even)for j in abc)
        if all((s[i] in j[0] and j[2]=='up') or (s[i] in j[1] and j[2]=='down') or \
            (s[i] not in j[0] + j[1] and j[2]=='even') for j in abc):
            print(f'{s[i]} is the counterfeit coin and it is heavy.')
            break
        if all((s[i] in j[0] and j[2]=='down') or (s[i] in j[1] and j[2]=='up') or \
            (s[i] not in j[0] + j[1] and j[2]=='even') for j in abc):
            print(f'{s[i]} is the counterfeit coin and it is light.')
            break
#    except EOFError:
#        break