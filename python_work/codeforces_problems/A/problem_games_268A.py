n=int(input())
#group={}
num=0
#for _ in range(n):
#    hi,ai=map(int,input().split())
#    group[hi]=ai
#for h in group.keys():
#    for a in group.values():
#        if h==a:
#            num+=1
#print(num)
h=[]
a=[]
for _ in range(n):
    hi,ai=map(int,input().split())
    h.append(hi)
    a.append(ai)
for i in h:
    for j in a:
        if i==j:
            num+=1
print(num)

