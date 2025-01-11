y,m,d=map(int,input().split('-'))
n=int(input())
day_of_month=[
    [0,31,28,31,30,31,30,31,31,30,31,30,31],
    [0,31,29,31,30,31,30,31,31,30,31,30,31]
]
def is_leap(y):
    return y%400==0  or (y%4==0 and y%100!=0)
for _ in range(n):
    d+=1
    if d>day_of_month[is_leap(y)][m]:
        m+=1;d=1
    if m>12:
        m=1;y+=1
if m<=9:
    m='0'+str(m)
if d<=9:
    d='0'+str(d)
print('-'.join(map(str,[y,m,d])))