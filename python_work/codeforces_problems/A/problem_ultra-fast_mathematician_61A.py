output=[]
a=list(map(int,input()))
b=list(map(int,input()))
for i in range(len(a)):
    if a[i] == b[i]:
        output.append(0)
    else:
        output.append(1)
print(''.join(map(str,output)))