import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest_path: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            ret = 0
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.left and root.val == root.left.val:
                ret += left + 1
                left += 1
            else:
                left = 0
            if root.right and root.val == root.right.val:
                ret += right + 1
                right += 1
            else:
                right = 0
            self.longest_path = max(self.longest_path, ret)
            return max(left, right)
        dfs(root)
        return self.longest_path




if __name__ == '__main__':
    root = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))
    s = Solution()
    print(s.longestUnivaluePath(root))