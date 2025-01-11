n=int(input())
nums=list(map(int,input().split()))
new_order=[nums.index(i)+1 for i in range(1,n+1)]
print(' '.join(map(str,new_order)))

#n = int(input())  # Number of friends
#p = list(map(int, input().split()))  # List of gifts received by each friend

#givers = [0] * n  # Initialize a list to store the result

#for i in range(n):
#    givers[p[i] - 1] = i + 1

#print(" ".join(map(str, givers)))