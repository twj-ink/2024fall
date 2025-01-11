'''Recursion
波兰表达式 http://cs101.openjudge.cn/2024fallroutine/02694
'''
d='+-*/'
s=input().split()
def operate():
    curr=s.pop(0)
    if curr in d:
        return str(eval(operate()+curr+operate()))
    else:
        return curr
print(format(float(operate()),'.6f'))

# '''stack
# 波兰表达式 http://cs101.openjudge.cn/2024fallroutine/02694
# 倒序即可使用栈，数字压入，遇到运算符弹出两个运算再压入
# '''
# d='+-*/'
# #print('1'.isdigit())
# s=list(input().split())
# s.reverse()
# stack=[]
# for i in s:
#     if i not in d:
#         stack.append(i)
#     else:
#         stack.append(eval(f'{stack.pop()}{i}{stack.pop()}'))
# print(format(stack[0],'.6f'))