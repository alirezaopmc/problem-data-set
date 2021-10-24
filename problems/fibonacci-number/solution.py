class Solution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]
        
# Contributed by LeetCode user mereck.
class Solution2:
    def fib(self, N: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))

n = int(input())
p = Solution().fib(n)
print(p)