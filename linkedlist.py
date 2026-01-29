class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def createbt(arr,i,n):
    if i>n:
        return None
    root=TreeNode(arr[i-1])
    root.left=createbt(arr,2*i,n)
    root.right=createbt(arr,2*i+1,n)
    return root
def preorder(root):#nlr
    if root is None:
        return
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)
def inorder(root):#lnr
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)
def postorder(root):#lrn
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value,end='')
def leverorder(root):
    if root is None:
        result=[]
        queue=[]
        queue.append(root)
        while queue:
            result.append(queue[0].val)
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


    arr=[3,4,5,6,7]
    n=len(arr)
    root=createbt(arr,1,n)
    print(leverorder(root))
    