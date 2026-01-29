'''def bfs_matrix(graph,start):
    n=len(graph)
    queue=[start]
    visited=[False]*n
    visited[start]=1
    while queue:
        node=queue.pop(0)
        print(node,end=' ')
        for adjacent in graph[node]:
            if visited[adjacent]==False:
                visited[adjacent]=1
                queue.append(adjacent)
graph=[
    [0,1,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,0,1,0],
    [0,1,0,0,0,1],

]
bfs_matrix(graph,0)'''
def bfs_matrix(graph,start):
    n=len(graph)
    queue=[start]
    visited=[False]*n
    visited[start]=1
    while queue:
        node=queue.pop(0)
        print(node,end=' ')
        for adjacent in graph[node]:
            if visited[adjacent]==False:
                visited[adjacent]=1
                queue.append(adjacent)
graph=[
     [1,2],
     [0,3],
     [0,1],
     [1,2],

]
bfs_matrix(graph,0)