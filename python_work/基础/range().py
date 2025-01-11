print(list(range(-3,21,2)))  #输出[-3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

square=[]
for i in range(1,21):
    print((square.append(str(i))))    #输出None，因为.append()只是添加无返回值

for i in range(1,21):
    square.append(str(i))
print(square)

#列表解析
a=[w for w in range(1,11,3)]
print(a)

for i in a:
    if i==7:
        break
    else:
        print(i)