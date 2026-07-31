# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_val = 0
    depth = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
                # Base case: empty tree/node has depth 0
        if not root:
            return 0

        # Recursively find max depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Current node adds 1 to the max of its children
        return 1 + max(left_depth, right_depth)