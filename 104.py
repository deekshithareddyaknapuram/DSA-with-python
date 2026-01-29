class Sol:
    def maxDepth(self,root):
        if not root:
            return 0
        c=0
        q=collections.deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            c+=1
        return c