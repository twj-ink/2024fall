a=list(map(int,input().split()))
s=list(input())
num=0
for i in s:
    num+=a[int(i)-1]
print(num)