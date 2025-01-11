n=int(input())

current_passengers=0
max_capacity=0

for i in range(n):
    ai,bi=map(int,input().split())
    current_passengers-=ai
    current_passengers+=bi
    max_capacity=max(max_capacity,current_passengers)
print(max_capacity)
