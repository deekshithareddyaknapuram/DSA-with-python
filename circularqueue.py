class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=self.rear=-1
    def enqueue(self,data):
        if(self.rear+1)%self.size==self.front
         