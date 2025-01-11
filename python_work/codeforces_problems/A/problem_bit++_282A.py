n=int(input())
count=0
for _ in range(n):
    line=input().strip()
    if '++' in line:
        count+=1
    elif '--' in line:
        count-=1
print(count)

#x+=1   ->  x=x+1
#x-=1   ->  x=x-1
#x//=10 ->  x=x//10 (删除末位的0)