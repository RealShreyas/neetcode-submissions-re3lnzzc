# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        def dfs(root):
            if not root:
                return 0
            
            depth_l = dfs(root.left)
            depth_r = dfs(root.right)
            mp[max(depth_l, depth_r) + 1].append(root.val)
            return (max(depth_l, depth_r)+1)
        
        dfs(root)
        return list(mp.values())