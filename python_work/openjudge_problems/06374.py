n=int(input())
s=list(map(str,input().split()))
output=[]
current_line=''
for i in s:
    if len(current_line+i)<=80:
        current_line=current_line+i+' '
    else:
        current_line=current_line.strip()
        output.append(current_line)
        current_line=i+' '
a=current_line.strip()
output.append(a)
for i in output:
    print(i)
