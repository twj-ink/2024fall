#不可变性：一旦创建，元组的内容不能更改。
#有序性：元组中的元素是有序的，按添加的顺序排列。

a=(1,2)
new_list=list(a)
print(new_list)
new_list[0]=3
a=tuple(new_list)
print(a)

squares=tuple(x**2 for x in range(1,5))
print(squares)