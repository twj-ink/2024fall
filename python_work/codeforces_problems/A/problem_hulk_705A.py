n=int(input())
start='I hate '
for i in range(2,n+1):
    if i%2==0:
        start+='that I love '
    else:
        start+='that I hate '
print(start+'it')