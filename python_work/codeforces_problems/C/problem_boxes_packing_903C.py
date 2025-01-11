from collections import Counter
n=int(input())
a=list(map(int,input().split()))
counter_a=Counter(a)
s=max(counter_a.values())
print(s)