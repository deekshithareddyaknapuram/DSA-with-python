def isBalanced(root):
    def help(node):
        if not node:
            return 0
        left=help(node.left)
        right=help(node.right)
        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
    return help(root)!=-1
