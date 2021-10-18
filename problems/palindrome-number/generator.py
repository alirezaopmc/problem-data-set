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
    yes_odd = 1
    yes_even = 2
    no = 3

    ch = rnd(1, 3)
    n = None

    if ch == yes_odd:
        n = rnd(0, 10 ** 4)
        n = str(n) + ''.join(list(reversed(list(str(n)))))
    
    if ch == yes_even:
        n = rnd(0, 10 ** 4)
        n = str(n) + ''.join(list(reversed(list(str(n)[:-1]))))
    
    if ch == no:
        n = rnd(0, 10**9)
        while isPalindrome(str(n)):
            n = rnd(0, 10**9)
        n = str(n)

    inputs = n
    outputs = 'NO' if ch == no else 'YES'

    return inputs, outputs

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
    n = 212
    
    inString = "{}\n".format(
        n
    )

    outString = "YES"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 516
    
    inString = "{}\n".format(
        n
    )

    outString = "NO"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(98):
    print(i)
    inputs, outputs = generate()

    n = inputs
    ans = outputs

    inString = "{}\n".format(
        n
    )

    outString = "{}\n".format(
        ans
    )

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")