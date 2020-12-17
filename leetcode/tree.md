+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)
## Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
```python
def maxDepth(self, root: TreeNode) -> int:
    def travel(node):
        if not node:
            return 0
        l=r=0
        if node.left:
            l = travel(node.left)
        if node.right:
            r = travel(node.right)
        return 1+max(l,r)
    return travel(root)
```
## Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    return_list = []
    stack = []
    node = root
    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        elif(stack):
            node = stack.pop()
            return_list.append(node.val)
            node = node.right
        else:
            break
    return return_list
```
## Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return root
    tmp = root.left
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(tmp)
    return root
```
## Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return root
    queue=[]
    queue.append(root)
    ans=[]
    while queue:
        l=len(queue)
        level=[]
        while l!=0:
            node= queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            l=l-1
        ans.append(level)
    return ans   
```
## Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python
def inord(self, node, A):
    if node.left:
        self.inord(node.left,A)
    A.append(node.val)
    if node.right:
        self.inord(node.right,A)
    return A
def kthSmallest(self, root: TreeNode, k: int) -> int:
    A = []
    res = self.inord(root,A)
    return res[k-1]
```
## Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
```python
def isValidBST(self, root: TreeNode) -> bool:
    stack = []
    cur = root
    vals = []
    while(stack or cur):
        while(cur):
            stack.append(cur)
            cur=cur.left
        cur = stack.pop()
        vals.append(cur.val)
        cur = cur.right
    return sorted(list(set(vals))) == vals
```
## Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python
def isSymmetric(self, root: TreeNode) -> bool:
    path = []
    def euler(node):
        if not node: path.append(None); return
        path.append(node.val)
        euler(node.left)
        path.append(node.val)
        euler(node.right)
        path.append(node.val)
    euler(root)
    return path == path[::-1]
```