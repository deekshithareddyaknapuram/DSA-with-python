def help(t1,t2):
    if not t1 and not t2:
        return True
    if not t1 and t2:
        return True
    if t1.val!=t2.val:
        return False
    left=help(t1.left,t2.right)
    right=help(t1.right,t2.left)
    if left and right:
        return True
    else:
        return False
return help(root.left,root.right)