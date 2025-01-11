n=int(input())
num=0
list=[]
for _ in range(n):
    magnet=int(input())
    list.append(magnet)
for i in range(0,n-1):
    if list[i]!=list[i+1]:
        num+=1
print(num+1)

#list=[input() for _ in range(n)]
