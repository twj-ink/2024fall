s=input()
upper_num=sum(1 for c in s if c.isupper())
lower_num=sum(1 for c in s if c.islower())  #lower_num=len(s)-upper_sum
if upper_num > lower_num:
    print(s.upper())
else:
    print(s.lower())

#for c in s:
#这部分是一个生成器表达式，它遍历字符串 s 中的每一个字符 c。

#if c.isupper():
#这个条件检查当前字符 c 是否为大写字母。c.isupper() 是一个字符串方法，当 c 是大写字母时返回 True，否则返回 False。

#1:
#如果条件 if c.isupper() 为真（即当前字符 c 是大写字母），则生成器表达式会生成一个值 1。

#sum(...):
#最后，sum() 函数对生成器表达式产生的所有 1 进行求和，得到字符串 s 中大写字母的总数。

#count=0
#for c in s:
#    if c.isupper():
#        count+=1
#count2=len(s)-count