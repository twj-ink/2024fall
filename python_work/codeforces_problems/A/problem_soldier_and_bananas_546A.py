k,n,w=map(int,input().split())
need=(((w+1)*w)/2)*k
if n < need:
    print(int(need-n))
else:
    print(0)
