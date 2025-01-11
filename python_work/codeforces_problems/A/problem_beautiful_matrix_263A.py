#row -> 行   column -> 列
row=0
col=0
for i in range(5):
    line=list(map(int,input().split()))
    if 1 in line:
        row=i+1
        col=line.index(1)+1
moves=abs(row-3)+abs(col-3)
print(moves)

#.index()的使用：用于查找某个值在列表或字符串中第一次出现的位置
#s.index(substring, start, end)  s.index('hello',0,5)

#abs()的使用：即绝对值
