import collections
import functools
import re
import sys
from typing import List




class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ret = [[]]
        for num in sorted(nums):
            tmp = []
            for subset in ret:
                if not subset or num % subset[-1] == 0:
                    tmp.append(subset + [num])
            ret.append(max(tmp, key=len))
        return max(ret, key=len)


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([3, 4, 16, 8]))