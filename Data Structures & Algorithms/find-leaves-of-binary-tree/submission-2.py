# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node):
            if not node:
                return 0
            
            # Calculate height (distance from bottom)
            height = max(dfs(node.left), dfs(node.right)) + 1
            
            # If this is the first time we've reached this height, 
            # add a new sub-list to our results
            if height > len(res):
                res.append([])
            
            # height 1 goes to index 0, height 2 to index 1, etc.
            res[height - 1].append(node.val)
            return height
            
        dfs(root)
        return res