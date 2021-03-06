def isPalindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            return False
    return True

n = input()

if isPalindrome(n):
    print('YES')
else:
    print('NO')