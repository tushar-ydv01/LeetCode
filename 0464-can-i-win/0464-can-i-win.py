class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):

        if desiredTotal <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        memo = {}

        def solve(used, current):

            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):

                if not (used & (1 << i)):

                    if current + i >= desiredTotal:
                        memo[used] = True
                        return True

                    if not solve(used | (1 << i), current + i):
                        memo[used] = True
                        return True

            memo[used] = False
            return False

        return solve(0, 0)