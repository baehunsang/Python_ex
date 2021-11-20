import collections
import functools
import re
import sys
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        depth = 0
        Q = collections.deque([root])
        while Q:
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            depth += 1
        return depth



if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode((15)), TreeNode(7)))
    s = Solution()
    print(s.maxDepth(root))