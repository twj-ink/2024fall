def josephus(n,m):
    if n == 1:
        return 0
    else:
        return (josephus(n-1,m)+m)%n

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    result=josephus(n,m)+1  # +1 转换为 1-based index
    print(result)

