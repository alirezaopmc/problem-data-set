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

def generate(i): 
    mylist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    s = random.randint(100,2147483647)
    out =s
    result = ""
    while(s):
        rem = s % 26
        s = s//26
        result += mylist[rem-1]
        if(rem==0):
            s-=1
            
    return result[::-1],out

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
    n = 'A'
    
    inString = "{}\n".format(
        n
    )

    outString = "1\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = "AB"
    
    inString = "{}\n".format(
        n
    )

    outString = "28\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
if "Case 3":
    n='FXSHRXW'
    inString = "{}\n".format(
        n
    )
    outString = "2147483647\n"
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