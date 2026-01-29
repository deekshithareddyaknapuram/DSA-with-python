class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def create_bst(root,val):
    if root is None:
        return TreeNode(val)
    else:
        if root.val==val:
            return
        elif root.val<val:
            root.right=create_bst(root.right,val)
        else:
            root.left=create_bst(root.left,val)
    return root
def preorder(root):
    if root is None:
        return
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)
arr=[8,3,10,6,14,4,7]
root=TreeNode(arr[0])
for i in range(1,len(arr)):
    root=create_bst(root,arr[i])
print(create_bst)
preorder(root)
