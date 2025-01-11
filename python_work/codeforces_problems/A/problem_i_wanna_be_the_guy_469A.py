n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
del p[0]
del q[0]
total=set(p+q)
if len(total)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')