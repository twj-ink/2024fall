n,k=map(int,input().split())
persons=list(map(int,input().split()))
num=sum(1 for i in persons if i+k<=5)
print(int(num//3))