# using hash table
# Time complexity : O(n). We do search() and insert() for nnn times and each operation takes constant time.
#Space complexity : O(n). The space used by a hash table is linear with the number of elements in it.
def solution(s):
    dic = set()
    lst = s.split()
    for item in lst :
        if item in dic :
            return True
        dic.add(item)
    return False

n = input()
print(solution(n))