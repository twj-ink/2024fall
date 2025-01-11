message='Hello,world!'  #message是变量，字符串要用''或""引住
#\n是换行符也属于字符串  +连接字符串或变量  print()是函数  .title()是方法
print(message+'\n'+message.title()+'\n'+message.upper()+'\n'+message.lower())
print('\n\t'+message+'It is time to enjoy yourself!')  #\t是制表符，空格

#使用方法.lstrip() .rstrip() .strip()来删除空格
a=' 123 '
print('\n'+a.lstrip()+'\n'+a.rstrip()+'\n'+a.strip())

#数字可+-*/运算，**表示幂  用函数str()让数字变成字符串
print(1+1)
age=23
#print('This is your '+age+'rd birthday') 是错误的
print('This is your '+str(age)+'rd birthday')

#列表的值的检索 替换 增添 删除 (使用复数形式便于辨别)
numbers=['3','4','1','2']
print(numbers[0]+'\n'+numbers[1])  #此处为检索的一个字符串可做加法
print(numbers[0:4])                #此处为一个切片，是一个数组，不可做加法
print(numbers[0]+'\n\t'+' '.join(numbers))
print(','.join(numbers))

numbers[0]='5'
print(numbers)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
copyed_players=players[:]           #用于复制列表
print(copyed_players)
