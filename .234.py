def kk(head):
    if not head or not head.next:
        return True
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    prev=None
    curr=slow
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    l,r=head,prev
    while r:
        if l.val!=r.val:
            return False
        l=l.next
        r=r.next
    return True
print(kk(head))






