

# Is Prime?
def isPrime(n):
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

n = int(input())

ans = [-1, -1]
for i in range(n - 1 + n%2, 2, -2):
    if isPrime(i) and isPrime(i-2):
        ans = [i-2, i]
        break

print(*ans)