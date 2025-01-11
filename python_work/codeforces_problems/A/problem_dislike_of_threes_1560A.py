def liked_nums(n,m):
    n=[]
    for i in range(1,1667):
        if i%3==0 or i%10==3:
            continue
        else:
            n.append(i)
    return n[m-1]

n=[]
t=int(input())
for _ in range(t):
    m=int(input())
    print(liked_nums(n,m))