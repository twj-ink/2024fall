n=int(input())
s=bin(n)[2:]
print('Yes' if s==s[::-1] else 'No')