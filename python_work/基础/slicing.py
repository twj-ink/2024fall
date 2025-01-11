#s[start:stop:step]
s = "hello world"

# 切片的不同用法：
print(s[1:5])   # 输出: "ello"，从索引 1 开始，到索引 5（不包含 5），即 "ello"
print(s[:5])    # 输出: "hello"，从开头到索引 5（不包含 5），即 "hello"
print(s[6:])    # 输出: "world"，从索引 6 开始到字符串结尾，即 "world"
print(s[::2])   # 输出: "hlo wrd"，从头到尾，每隔一个字符取一次
print(s[::-1])  # 输出: "dlrow olleh"，反转字符串