#map()函数作为迭代器，可将一个函数对多个对象处理，最后要用1ist()或for显示结果
def square(x):
    return x**2

numbers=[1,2,3]
squared_numbers=map(square,numbers)  #map()返回的是一个迭代器，迭代器只能被遍历一次。
print(list(squared_numbers))         #当调用list(squared_numbers)时,迭代器中的所有元素都被消耗并转化为列表 [1, 4, 9],并打印出来。

for num in squared_numbers:
    print(num)                       #因为迭代器已经被消耗完了，所以当再试图遍历 squared_numbers 时，不会有任何输出。

#如果需要多次遍历结果，可以在第一次将 squared_numbers 转换为列表并保存
def square(x):
    return x**2

numbers=[1,2,3]
squared_numbers=list(map(square,numbers))
print(squared_numbers)               #输出[1,4,9]

for num in squared_numbers:
    print(','.join(str(num)))        #.join()对每一个num单独数字操作故没有逗号，输出1\n4\n9

print(','.join(str(num) for num in squared_numbers))   #.join()对列表内的所有数字操作，输出1,4,9
