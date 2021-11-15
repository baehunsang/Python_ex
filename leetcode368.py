import collections
import functools
import re
import sys
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = []
        i = 0
        for num in nums:
            if len(dp) == 0:
                dp.append([num])
                continue
            if all(map(lambda x: x % num == 0 or num % x == 0, dp[i])):
                dp.append(dp[i]+ [num])
                i += 1
        return dp[-1]



if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([1, 2, 3, 4]))