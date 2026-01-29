from collections import deque
def reverse_first_k(q,k):
    solve(q,k)
    s=len(q)-k
    for i in range(s):
        x=q.popleft()
        q.append(x)
    return q
def solve(q,k):
    if k==0:
        return
    e=q.popleft()
    solve(q,k-1)
    q.append(e)
queue=deque([1,2,3,4,5,6,7,8,9,10])
k=5
queue=reverse_first_k(queue,k)
while queue:
    print(queue.popleft(),end=' ')
    
