s=input().strip()
numbers=s.split('+')
output=sorted(numbers,key=int)
print('+'.join(output))

#将数字按大小排序：sorted_numbers=sorted(numbers,key=int)