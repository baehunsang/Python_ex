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
    diameter: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return self.diameter




if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    s = Solution()
    print(s.diameterOfBinaryTree(root))