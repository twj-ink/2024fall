n,m,k=map(int,input().split())
a=[[0]*(m+2) for _ in range(n+2)] #加保护圈
def check(i,j):
    if a[i][j + 1] and a[i + 1][j] and a[i + 1][j + 1]:
        return True
    if a[i][j - 1] and a[i + 1][j - 1] and a[i + 1][j]:
        return True
    if a[i - 1][j] and a[i - 1][j + 1] and a[i][j + 1]:
        return True
    if a[i - 1][j - 1] and a[i - 1][j] and a[i][j - 1]:
        return True
    return False
cnt=1
for _ in range(k):
    i,j=map(int,input().split())
    a[i][j]=1
    if check(i,j):
        print(cnt)
        break
    else:
        cnt+=1
else:
    print(0)