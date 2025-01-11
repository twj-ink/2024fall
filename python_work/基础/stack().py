'''匹配(){}[]'''

def match(a,b):
    l='([{';r=')]}'
    return l.index(a)==r.index(b)

def parchecker(s):
    flag=True
    stack=[]
    for i in s:
        if i in '([{':
            stack.append(i)
        else:
            if stack and match(stack[-1],i):
                stack.pop()
            else:
                flag=False
    if not stack and flag:
        return True
    else:
        return False

s=input()
print(['NO','YES'][parchecker(s)])

'''十进制转换成任意进制'''
def baseconverter(num,base):
    digits='0123456789ABCDEF'
    stack=[]
    ans=''
    while num>0:
        rem=num%base
        stack.append(digits[rem])
        num//=base
    while stack:
        ans+=str(stack.pop())
    return ans
n=int(input())
print(baseconverter(n,16))

'''将中序表达式转为后序表达式'''
import string
def m_to_r_converter(s):
    order={'*':3,'/':3,'+':2,'-':2,'(':1}
    ans=''
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        elif i in string.ascii_uppercase:
            ans+=i
        elif i==')':
            x=stack.pop()
            while x!='(':
                ans+=x
                x=stack.pop()
        elif i in order:
            while stack and order[i]<=order[stack[-1]]:
                ans+=stack.pop()
            stack.append(i)
    while stack:
        ans+=stack.pop()
    return ans

s=input()
print(m_to_r_converter(s))