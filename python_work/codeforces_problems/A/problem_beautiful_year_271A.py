y=int(input())
output=y+1
active=True
while active:
    if len(set(str(output))) != len(str(output)):
        output+=1
    else:
        break
print(output)













#判断字符串里有没有相同的字符，采用set()和len()