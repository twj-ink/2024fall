#from collections import Counter
from math import ceil

n=int(input())
s=list(map(int,input().split()))
#counter_s=Counter(s)
#for i in range(1,5):
#    if i not in counter_s:
#        counter_s[i]=0
#a,b,c,d=counter_s[1],counter_s[2],counter_s[3],counter_s[4]
a,b,c,d=[s.count(i) for i in range(1,5)]
taxi=c+d+ceil(b/2)
space_for_a=c+(0 if b%2==0 else 2)
if a>space_for_a:
    taxi+=ceil((a-space_for_a)/4)
print(taxi)