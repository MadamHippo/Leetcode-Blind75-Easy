'''
#112 Path Sum

https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
    #iterative method
        
        if not root: 
            return False
        
        # keep track of root node, and sum
        stack = [(root, targetSum)]
        
        while stack:
            
            
            current_node, targetSum = stack.pop()
            if not current_node.left and not current_node.right and current_node.val == targetSum:
                return True
            
            if current_node.left:
                stack.append((current_node.left, targetSum - current_node.val))
            if current_node.right:
                stack.append((current_node.right, targetSum - current_node.val))
        
        return False
        
        
        
    
        ''' 
        
        # Recursive method #1 :
        
            # Time: O(n) ... n is # of nodes in tree
            # Space: O(h) ... height of tree...or O(logn)
            
            # subtracing current node's value from targetSum.
            # if haven't found path, ask the children.
            # once we have gone through all the nodes, then return false.
            # if we have found a leaf that matches target - sum then return true.
        
        # if there's no root node:
        # Base Case to stop the recursion:
        if not root:
            return False
            
        
        # if there's no left and right root AND the sum - value is 0 then path to leaf sum was found.
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum = targetSum - root.val
        
        # Otherwise, pass recursive call to children...call the function recursively and ask if root.left's path can find the targetSum or if root.right can find the targetSum.
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
        # example, starts at 5.
        # substract 5 - 22 = 17
        # hey now is there a sum of 17?
        # ask left child of the node, and right child of node...
        # until it's the end...now if the root is null
        
        '''
        
        
        
        '''
        Recursion #2
        
        # base case to catch if no children
        
        if root.left is None and root.right is None:
            return root.val
        
        if root is None:
            return 0
        
        
        maxChildPathSum = max(hasPathSum(root.left), hasPathSum(root.right))
        
        return root.val + maxChildPathSum
        
        '''
        
        
        
