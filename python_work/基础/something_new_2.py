a={1,2,3}
b={2,3,4}
a.update(b)
print(a)
a.intersection_update(b)
print(a)
a.difference_update(b)
print(a)
a={1,2,3}
a.symmetric_difference_update(b)
print(a)

c={'name':1,'age':2}
print(c.values())
print(c.get('nam','alt')) #Returns the value associated with 'nam', 'alt' otherwise

