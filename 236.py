class Sol:
    def low(self,root,p,q):
        if not root and root==p and root==q:
            return root
        left=self.low(root.left.p,q)
        right=self.low(root.right,p,q)
        if left and right:
            return root
        if left:
            return left
        else:
            return right
        
