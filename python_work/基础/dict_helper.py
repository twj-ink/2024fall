#字典由键-值对构成
dict={'a':'1','b':'2','c':'3'}
print(dict['a'])  #访问 输出1

dict['d']='4'
print(dict)       #添加 输出{'a': '1', 'b': '2', 'c': '3', 'd': '4'}

dict['a']='5'
print(dict)       #修改 输出{'a': '5', 'b': '2', 'c': '3', 'd': '4'}

del dict['a']
print(dict)       #删除 输出{'b': '2', 'c': '3', 'd': '4'}

squares={x:x**2 for x in range(1,5)}
print(squares)

#遍历键-值对
for key,value in dict.items():
    print('\nKey:'+key)
    print('Value'+value)

#遍历键
for key in dict.keys():
    print(key)

for k in sorted(dict.keys()):
    print(k)

#遍历值
for value in dict.values():
    print(value)
for v in set(dict.values()):    #set()集合将重复项剔除
    print(v)

aliens=[]
for alien_number in range(4):
    new_alien={'color':'green','size':'big'}
    aliens.append(new_alien)

print(aliens)
print(len(aliens))              #range(4)创建了一个从0到3的序列，长度为4
print(alien_number)             #alien_number是一个循环值，打印结果是最后一次的值，即3

# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

#在字典中嵌套列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title()+"'s favorite language is:\n\t"+languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

#在字典中嵌套字典
users={
    'mike':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'john':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for user_name,user_info in users.items():
    print('\nUser_name:'+user_name)
    print('\tFull_name:'+user_info['first'].title()+' '+user_info['last'].title())
    print('\tLocation:'+user_info['location'])








