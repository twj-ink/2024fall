n=int(input())
s=input().upper()
sum_a=sum(1 for i in s if i=='A')
sum_d=sum(1 for j in s if j=='D')
if sum_a > sum_d:
    print('Anton')
elif sum_a < sum_d:
    print('Danik')
elif sum_a == sum_d:
    print('Friendship')

#sum()的使用：数出字符串中满足条件的字符的个数