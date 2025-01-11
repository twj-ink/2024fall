n=int(input())
p=list(map(int,input().split()))
total=sum(i for i in p)
print((total/(len(p)*100))*100)