def exclude7(x):
    return x!='7'
def is_unrelated7(x):
    return all(exclude7(i) for i in str(x)) and int(x)%7!=0

n=str(input())
a=0
for i in range(1,int(n)+1):
    if is_unrelated7(i):
        a+=i**2
print(a)