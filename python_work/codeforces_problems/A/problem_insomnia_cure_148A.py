num=[]
for _ in range(4):
    i=int(input())
    num.append(i)
d=int(input())
total=[]
for j in num:
    j_list=[j for j in range(j,d+1,j)]
    total.extend(j_list)
print(len(set(total)))

###转化成同余问题
# Read input values
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damaged_dragons = 0

# Check each dragon
for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        damaged_dragons += 1

print(damaged_dragons)

