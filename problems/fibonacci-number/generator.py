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
cache = {0: 0, 1: 1}
def fib(N: int) -> int:
    if N in cache:
        return cache[N]
    cache[N] = fib(N - 1) + fib(N - 2)
    return cache[N]
    
    

def generate(i): 
        return i,fib(i)
        

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


    
# Automatically add inputs
for i in range(50):
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