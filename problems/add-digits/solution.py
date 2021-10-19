
def addDigits( num: int) -> int:
    return 1 + (num - 1) % 9 if num else 0

n= input()
n= int(n)
print (addDigits(n))
