def get_min_num(n,k):
    stack=[]
    for i in n:
        while stack and k and stack[-1]>i:
            curr=stack.pop()
            k-=1
        stack.append(i)
    while k:
        stack.pop()
        k-=1
    return ''.join(map(str,stack))
t=int(input())
for _ in range(t):
    n,k=input().split()
    new_num=get_min_num(n,int(k))
    print(new_num)