# inputs
n, k = int(input()), int(input())

# result inits with n in it
res = n

# loop k times and add to res
for i in range(k): res += n * 10 ** (i + 1)

# output
print(res)