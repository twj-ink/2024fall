M,N=map(int,input().split())
if N%2==0:
    print(int(M*(N/2)))
else:
    if M%2==0:
        print(int(M*((N-1)/2)+M/2))
    else:
        print(int(M*((N-1)/2)+(M-1)/2))

M, N = map(int, input().split())

# Calculate the maximum number of dominoes
max_dominoes = (M * N) // 2  #//取结果的整数部分

# Output the result
print(max_dominoes)
