class Stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack)==0
    def push(self,item):
        self.stack.append(item)
        print(f'pushed{item} to the stack')
    def pop(self):
        if self.is_empty():
            print('stcack is empty.cannot pop')
            return None
        item=self.stack.pop()
        print(f'popped{item} from the stack')
        return item
    def peek(self):
        if self.is_empty():
            print(f'stack is empty.cannot peek')
            return None
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        if self.is_empty():
            print('stack is empty')
        else:
            print('stack',self.stack)
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print('top element:',stack.peek())
stack.pop()
stack.pop()
stack.display()
