c=0
res=None
def inorder(node):
    nonlocal c
    nonlocal res
    # k=int(input())
    if root:
        inorder(node.left)
        c+=1
        if c==k:
            res=root.val
        inorder(root.right)
inorder(root)
return res




