n=int(input())
bill=0
bill+=n//100
n%=100
bill+=n//20
n%=20
bill+=n//10
n%=10
bill+=n//5
n%=5
bill+=n
n%=1
print(bill)