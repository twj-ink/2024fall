n=int(input())
def is_lucky_digit(x):
    return x=='4' or x=='7'
def is_lucky_number(c):
    return all(is_lucky_digit(x) for x in c)
total=sum(1 for i in str(n) if is_lucky_digit(i))
if is_lucky_number(str(total)):
    print('YES')
else:
    print('NO')

#all()的使用：字符串中的每一个字符都满足一个条件
#sum()的使用：数出字符串中满足条件的字符的个数