import random
import math
from essential_generators import DocumentGenerator
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
    gen = DocumentGenerator()
    input_s = gen.sentence()
    out = len(input_s.split()[-1])
    return input_s,out

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
    n = ' '*200
    
    inString = "{}\n".format(
        n
    )

    outString = "0\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = "ab hello ok!"
    
    inString = "{}\n".format(
        n
    )

    outString = "3\n"
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
if "Case 3":
    n='a a a a a a aaaa'
    inString = "{}\n".format(
        n
    )
    outString = "4\n"
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