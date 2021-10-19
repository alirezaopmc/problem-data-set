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



def isPalindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            return False
    return True

rnd = lambda minimum=0, maximum=10**9: random.randint(minimum, maximum)


count = 0
helper = None

def generate(i):
    i=random.randint(2**16,2**32)
    return i, 1 + (i - 1) % 9 if i else 0 
        
    
        
    
    

        

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
    n = 0
    
    inString = "{}\n".format(
        n
    )

    outString = "0\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 1
    
    inString = "{}\n".format(
        n
    )

    outString = "1\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
if "Case 3":
    n=2**32
    inString = "{}\n".format(
        n
    )
    outString = str(2**32%9)+'\n'
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
    
# Automatically add inputs
for i in range(47):
    print(i)
    inputs, outputs = generate(i)

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
