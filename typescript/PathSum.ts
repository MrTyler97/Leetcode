/*
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
*/
  
  
  
  class TreeNode {
      val: number
      left: TreeNode | null
      right: TreeNode | null
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.left = (left===undefined ? null : left)
          this.right = (right===undefined ? null : right)
      }
  }
 

function hasPathSum(root: TreeNode | null, targetSum: number): boolean{
    // DFS algo for searching each branch.

    // Helper function because we need to keep track of our sum
    function dfsSum(node: TreeNode | null, sum: number): boolean{
        // If tree is empty
        if (node === null){
            return false;
        }
        // add our value
        sum += node.val;
        // check for leaf node
        if (node.left == null && node.right == null){
            // if leaf node check for target
            if (sum === targetSum){
                return true;
            }
        }
        
        /* Recursively call left node then right node when base case is met 
        The  || operator ensure all paths are checked until a "true" value is found.*/

        // else -> DFS n add sum
        return dfsSum(node.left, sum) || dfsSum(node.right, sum)
    }
    return dfsSum(root, 0); 
};