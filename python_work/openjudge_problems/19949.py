n=int(input())
total=0
for _ in range(n):
    count3=count6=0
    s=input()
    for i in range(len(s)-2):
        if s[i:i+3]=='###':
            count3+=1
    for i in range(len(s)-6):
        if s[i:i+7]=='### ###':
            count6+=1
    total+=count3//2-count6
print(total)