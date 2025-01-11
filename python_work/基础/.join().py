#''.join()将括号里的字符串用''里的符号分隔，在一行打印
###括号内必须是字符串
numbers=[1,2,3]
print(','.join(str(num) for num in numbers))  #输出1,2,3

print(';'.join(str(numbers)))  #输出[;1;2;3;]

print(','.join(str(num) for num in numbers[-2:])) #遍历切片


