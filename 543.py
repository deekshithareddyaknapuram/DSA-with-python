class Sol:
    def dia(self,root):
        self.diameter=0
        def help(node):
            if not node:
                return 0
            left=help(node.left)
            right=help(node.right)
            self.diameter=max(self.diameter,left+right)
            return 1+max(left,right)
        help(root)
        return self.diameter
        