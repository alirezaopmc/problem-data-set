class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            result = result * 26
            result += (ord(s[i]) - ord('A') + 1)
        return result


class generate:
    mylist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    def generator(self, s: int) -> str:
        result = ""
        while(s>1):
           rem = s % 26
           s = s//26
           result += self.mylist[rem-1]
        return result[::-1]
ans = Solution()
s = input()
print(ans.titleToNumber(s))
#ans = generate()
#s = int(input())
#print(ans.generator(s))