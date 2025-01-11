#list()可将字符串，元组，字典中的键，集合转换成列表
a=list("hello")
print(a)               #输出['h', 'e', 'l', 'l', 'o']

b=(1,2,3)
list_b=list(b)
print(list_b)          #输出[1, 2, 3]

c={'name':'1'}
list_c=list(c)
print(list_c)          #输出['name']

squares=[x**2 for x in range(1,5) if x <4]
print(squares)         #输出[1, 4, 9, 16]

a='word'
a_list=list(a)
a_list.reverse()
a1=''.join(a_list)
print(a1)