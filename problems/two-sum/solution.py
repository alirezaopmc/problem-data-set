n, t = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) == t:
            print(i+1, j+1)
            exit()

print(-1, -1)