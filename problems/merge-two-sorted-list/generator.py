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

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def isPalindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


rnd = lambda minimum=0, maximum=10 ** 9: random.randint(minimum, maximum)

count = 0
helper = None


def generate(i):
    n = random.randint(1,50)
    lst1=[]
    for i in range(1,n):
        lst1.append(random.randint(-100,100))

    n = random.randint(1,50)
    lst2=[]
    for i in range(1,n):
        lst2.append(random.randint(-100,100))
    lst1.sort()
    lst2.sort()
    input = "{}{}{}{}{}{}{}".format(
        len(lst1),'\n',
        " ".join(str(x) for x in lst1),"\n",
        len(lst2),"\n",
        " ".join(str(x) for x in lst2),
    )
    output = []
    for i in lst1 :
        output.append(i)
    for i in lst2 :
        output.append(i)
    output.sort()
    output = " ".join(str(x) for x in output)
    

    return input , output



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
    n = """0
4
1 2 3 4 """

    inString = "{}\n".format(
        n
    )

    outString = "1 2 3 4\n"

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

if "Case 2":
    n = """2
11 13
0"""

    inString = "{}\n".format(
        n
    )

    outString = "11 13\n"

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(48):
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
