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

rnd = lambda minimum=0, maximum=10**9: random.randint(minimum, maximum)


count = 0
helper = None

def generate():
    n, t = rnd(2, 10**4), rnd(-10**9, +10**9)

    d = {}
    a = [ -1 for _ in range(n) ]

    for i in range(n):
        x = rnd(-10**9, +10**9)

        while (t-x) in d:
            x = rnd(-10**9, +10**9)

        a[i] = x 

    # Making only one solution    
    i = rnd(0, n-2)
    j = rnd(i+1, n-1)

    a[i] = t - a[j]

    inputs = (n, t, a)
    outputs = (i + 1, j + 1)

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
    n = 2
    t = 5
    a = [3, 2]
    
    inString = "{} {}\n{}\n".format(
        n, t,
        arrayToString(a)
    )

    outString = "1 2"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 5
    t =-7
    a = [-5, 11, -4, 3, 0]
    
    inString = "{} {}\n{}\n".format(
        n, t,
        arrayToString(a)
    )

    outString = "2 3"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(98):
    print(i)
    inputs, outputs = generate()

    n, t, a = inputs
    p, q = outputs

    inString = "{} {}\n{}\n".format(
        n, t,
        arrayToString(a)
    )

    outString = "{} {}\n".format(
        p, q
    )

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")