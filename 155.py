class MinStack:
    def __init__(self):
        self.st=[]
        self.minst=[]
    def push(self,val:int):
        self.st.append(val)
        if self.minst:
            val=min(val,self.minst[-1])
        self.minst.append(val)
        def pop(self):
            self.st.pop()
            self.minst.pop()
        def top(self):
            return self.st[-1]
        def getMin(self):
            return self.minst[-1]
        def display(self):
            print(self.st)
    ob=MinStack()
    ob.push(-2)
    ob.push(0)
    ob.push()
    ob.getmin()
    ob.display()
        
