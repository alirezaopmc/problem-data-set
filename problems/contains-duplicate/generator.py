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
    

rnd = lambda minimum=0, maximum=10**9: random.randint(minimum, maximum)


count = 0
helper = None
def solution(s):
    dic = set()
    lst = s.split()
    for item in lst :
        if item in dic :
            return True
        dic.add(item)
    return False


def generate(i): 
    lst = []
    length = random.randint(1,10**4)
    for i in range(0,length) :
        lst.append(random.randint(-10**7,10**7))
        
    lst = [str(int) for int in lst]
    inp =  " ".join(lst)
    return inp , solution(inp)
        
    

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
if "Case 0":
    n = '0 0'
    
    inString = "{}\n".format(
        n
    )

    outString = "True\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = "1"
    
    inString = "{}\n".format(
        n
    )

    outString = "False\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
if "Case 3":
    n='1 2 3 4'
    inString = "{}\n".format(
        n
    )
    outString = "False\n"
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