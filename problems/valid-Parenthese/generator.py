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
    stack = []
    s=""
    loop = random.randint(6,110)
    init = [")", "("]
    mapping = {")": "("}
    for i in range(1,loop) :
        s+=init[random.randint(0,1)]


    for char in s:

        if char in mapping:

            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return s,False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    return s, not stack
        
    
        
    
    

        

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
        "()"
    )

    outString = "True\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 1
    
    inString = "{}\n".format(
        '()[]{}'
    )

    outString = "True\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
if "Case 3":
    
    inString = "{}\n".format(
        '(]'
    )
    outString = 'False\n'
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
if "Case 4 " :
    inString = "{}\n".format(
        '([)]'
    )
    outString = 'False\n'
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

if "Case 5" :
    inString = "{}\n".format(
        '{[]}'
    )
    outString = 'True\n'
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

    
    
# Automatically add inputs
for i in range(45):
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
