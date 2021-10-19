def isPowerOfTwo(n):
        if n == 0:
            return False
        return n & (-n) == n

n = input()
n= int(n)
ans = isPowerOfTwo(n)
print(ans)
