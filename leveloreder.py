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
    print(root.val,end='')
def levelorder(root):
    if root is None:
        return
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
def search_in(root,ele):
    if root is None:
      return False
    if search(root.left,ele):
        return True
    if root.val==ele:
       return True
    return search(root.left,ele) or search(root.right,ele)

def search_post(root,ele):
    if root is None:
      return False
    if search(root.left,ele):
        return True
    if search(root.right,ele):
       return True
    return root.val==ele
    # return search(root.left,ele) or search(root.right,ele)
def search_level(root):
    if root is None:
        return
    queue=[]
    while queue:
        node=queue.pop(0)
        if node.val==ele:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False



arr=[3,4,5,6,7]
n=len(arr)
root=createbt(arr,1,n)
print(levelorder(root))
# postorder(root)
print(search_level(root,1))
    