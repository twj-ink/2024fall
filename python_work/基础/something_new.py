a='213hello'
print(a.center(10,'*'))
print(a)
print(a.count('l'))
print(a)
print(a.ljust(10,'*'))
print(a)
print(a.find('l'))
print(a)

aset={1,2,3}
bset={2,3,4}
c=aset|bset #并集
d=aset&bset #交集
e=aset-bset #差集
f=aset^bset #对称差集(不同时属于两集合的元素)
print(c,d,e,f,aset<=bset,aset>=bset)
g=aset.union(bset)
h=aset.intersection(bset)
i=aset.difference(bset)
j=aset.symmetric_difference(bset)
print(g,h,i,j,aset.issubset(bset),aset.issuperset(bset))

aset.add(5)
print(aset)
aset.discard(5) #移除指定元素，若元素不存在不会抛异常
aset.remove(1)  #移除指定元素，若元素不存在会抛出KeyError
k=aset.pop()      #随机移除并返回一个元素
print(aset,k)
bset.clear()
print(bset)