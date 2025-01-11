n=int(input())
points=list(map(int,input().split()))
a=0
current_max=points[0]
current_min=points[0]

for i in range(1,n):
    if points[i]>current_max or points[i]<current_min:
        a+=1
        current_max=max(current_max,points[i])
        current_min=min(current_min,points[i])
print(a)

