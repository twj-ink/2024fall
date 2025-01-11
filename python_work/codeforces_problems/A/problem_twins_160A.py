def the_first_sum(a,x):
    return sum(a[:x+1])
def the_last_sum(a,x):
    return sum(a[x+1:])

n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
num=0
for i in range(n):
    if the_first_sum(a,i) > the_last_sum(a,i):
        print(i+1)
        break
    else:
        continue

