am,an=map(int,input().split())
a=[list(map(int,input().split())) for i in range(am)]
bm,bn=map(int,input().split())
b=[list(map(int,input().split())) for i in range(bm)]
cm,cn=map(int,input().split())
c=[list(map(int,input().split())) for i in range(cm)]
if an!=bm or am!=cm or bn!=cn:
    print('Error!')
else:
    result=[[0]*bn for i in range(am)]
    for i in range(am):
        for j in range(bn):
            result[i][j]=sum(a[i][k]*b[k][j] for k in range(an))
    for i in range(cm):
        for j in range(cn):
            result[i][j]+=c[i][j]
    for i in result:
        print(' '.join(map(str,i)))
