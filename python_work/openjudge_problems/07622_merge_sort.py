cnt = 0
#统计的原理是：一旦发现了left[i]>right[j]，
#就说明left[i]之后是所有元素都会大于right[j]
#这一步的原理是left和right本身是有序的
#所有cnt+=len(left)-i
####相同，如果是正序数，就是cnt+=len(right)-j
def mergeSort(s):
    if len(s) == 1:
        return s  # 如果数组只有一个元素，直接返回
    mid = len(s) // 2
    left = mergeSort(s[:mid])  # 获取左部分排序
    right = mergeSort(s[mid:])  # 获取右部分排序
    return merge(left, right)  # 合并并统计调换次数

def merge(left, right):
    global cnt
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            cnt += len(left) - i  # 统计逆序对
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 主函数
input()
s = list(map(int, input().split()))
mergeSort(s)  # 执行排序
print(cnt)  # 输出调换次数
