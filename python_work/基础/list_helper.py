#列表的值的检索 替换 增添 删除 排序 长度(使用复数形式便于辨别)
numbers=['3','4','1','2']

numbers.append('6')                #与.sort()一样要单列一行
print(numbers)
#numbers.append(i for i in range(7,9))
#print(numbers)                    #append只会将生成器加入列表中，而不是生成器的结果
numbers.extend(i for i in range(7,9))
print(numbers)

numbers.insert(-1,'9')
print(numbers)

del numbers[:2]
print(numbers)

poped_number=numbers.pop()          #()里面不写默认从最后一位删除
print(' '.join(str(num) for num in numbers))

numbers.remove('1')
print(numbers)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))                 #暂时性排序
print(cars)

cars.sort()                         #永久性排序
print(cars)
cars.sort(reverse=True)             #倒序排序
print(cars)

cars_2 = ['Toyota', 'Honda', 'BMW']
result = cars.reverse()   #仅倒转顺序而无返回值

print(result)  # 输出: None
print(cars)    # 输出: ['BMW', 'Honda', 'Toyota']

print(len(cars))

squares=[x**2 for x in range(1,5)]
print(squares)         #输出[1, 4, 9, 16]
