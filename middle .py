class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Link:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newnode
    def middle(self):
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        # return slow

        p=0
        curr=self.head
        while curr:
            P+=1
            curr=curr.next
        mid=(p//2)
        curr=curr.head
        for _ in range(mid):
            curr=curr.next
        return curr
ll=Link()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
midi=ll.middle()
print(midi.data)

        