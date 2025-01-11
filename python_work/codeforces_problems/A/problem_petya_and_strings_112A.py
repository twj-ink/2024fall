string1=input().lower()
string2=input().lower()
if string1 == string2:
    print(0)
elif string1 > string2:
    print(1)
elif string1 < string2:
    print(-1)

a, b = input().lower(), input().lower()
print((a > b) - (a < b))
#(a>b)即a的字母表顺序在b的后面输出1，否则输出0