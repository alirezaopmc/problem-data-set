import random
import math

# Utility functions
def arrayToString(arr: list):
    result: str = ""

    for i in range(len(arr)):
        if i + 1 < len(arr):
            result += "{} ".format(arr[i])
        else:
            result += "{}".format(arr[i])
    
    return result
    
# Is Prime?
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    
    return True

def isPalindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            return False
    return True

rnd = lambda minimum=0, maximum=10**9: random.randint(minimum, maximum)


count = 0
helper = None

def generate():
    integer_d =  random.randint(1, 3500)
    num = integer_d
    val = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
    ]
    syb = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
    ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return integer_d,roman_num

        

def makeInputs(inString, cnt):
    path = "./in/input" + str(cnt) + ".txt"
    f = open(path, "w")
    f.write(inString)
    f.close()

def makeOutputs(outString, cnt):
    path = "./out/output" + str(cnt) + ".txt"
    f = open(path, "w")
    f.write(outString)
    f.close()

# Manually add some inputs
if "Case 1":
    n = 4
    
    inString = "{}\n".format(
        n
    )

    outString = "IV"
    
    count += 1
    makeInputs(outString, count)
    makeOutputs(inString, count)
    
if "Case 2":
    n = 1994
    
    inString = "{}\n".format(
        n
    )

    outString = "MCMXCIV"
    
    count += 1
    makeInputs(outString, count)
    makeOutputs(inString, count)

# Automatically add inputs
for i in range(48):
    print(i)
    inputs, outputs = generate()

    n = inputs
    ans = outputs

    inString = "{}\n".format(
      ans
    )

    outString = "{}\n".format(
       n
    )

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")