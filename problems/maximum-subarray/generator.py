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
    a = [ random.randint(-10000, 10000) for i in range(n) ]

    return (n, a)

def solveOut(inputs):
    (n, a) = inputs
    
    current_subarray = max_subarray = a[0]

    # Start with the 2nd element since we already used the first one.
    for num in a[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)

    return "{}\n".format(max_subarray)

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
    inputs = (1, [-3])
    
    inString = "{}\n{}\n".format(
        n, arrayToString([-3])
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 4
    inputs = (4, [101, -100, 10000, -1000, 1001])
    
    inString = "{}\n{}\n".format(
        n, arrayToString(inputs[1])
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(48):
    print(i)
    inputs = giveRandomInput()
    (n, a) = inputs

    inString = "{}\n{}\n".format(
        n, arrayToString(a)
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")