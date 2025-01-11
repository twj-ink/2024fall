n=int(input())
a=list(map(int,input().split()))
high=max(i for i in a)
low=min(i for i in a)
num1=a.index(high)
num2=a[::-1].index(low)
swaps=num1+num2
if num1+1 > len(a)-(num2+1):
    swaps-=1
print(swaps)