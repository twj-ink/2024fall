t=int(input())
n='Division '
for _ in range(t):
    rating=int(input())
    if rating<=1399:
        print(n+'4')
    elif rating<=1599:
        print(n+'3')
    elif rating<=1899:
        print(n+'2')
    else:
        print(n+'1')