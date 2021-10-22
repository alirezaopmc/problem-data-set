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

# Test-case generator template

count = 0

def giveRandomInput():
    n = random.randint(2, 10001)
    k = random.randint(0, n-1)
    a = [ random.randint(-10000, 10000) for i in range(n) ]

    return (n, k, a)

def solveOut(inputs):
    (n, k, a) = inputs
    
    ans = list(sorted(a))[n-k]

    return "{}\n".format(ans)

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
    n = 1
    k = 1
    a = [3]
    inputs = (n, k, a)
    
    inString = "{} {}\n{}\n".format(
        n, k, arrayToString(a)
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 5
    k = 3
    a = [10, 2, 2, 2, 2]
    inputs = (n, k, a)
    
    inString = "{} {}\n{}\n".format(
        n, k, arrayToString(a)
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(48):
    print(i)
    inputs = giveRandomInput()
    (n, k, a) = inputs

    inString = "{} {}\n{}\n".format(
        n, k, arrayToString(a)
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")