a=list(input())
i=0
new=[]
while i < len(a):
    if a[i] == '.':
        new.append('0')
        i+=1
    elif a[i] == '-' and i<len(a)-1:
        if a[i+1] == '-':
            new.append('2')
            i+=2
        else:
            new.append('1')
            i+=2
print(''.join(new))