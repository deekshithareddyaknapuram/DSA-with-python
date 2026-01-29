'''def dfs_adj_matrix(graph,start,visied=None):
     if visited is None:
       visited=set()
       visited.add(start)
       print(start,end=' ')
       for adjacent in range(len(garph)):
           if graph[start][adjacent]==1 and  adjacent not in visited:
              dfs_adj_matrix(graph,adjacent,visited) 


     
graph=[
    [1,1,1,1],
    [1,0,0,1],
    [1,0,0,1],
    [1,1,1,1],

]
print('\nDFS using adjacency Matrix:')
dfs_adj_matrix(graph,0)'''
def dfs_adj_list(graph,start,visied=None):
     if visited is None:
       
       visited=set()
       visited.add(start)
       print(start,end=' ')
       for adjacent in graph[start]:
           if adjacent not in visited:
              dfs_adj_list(graph,adjacent,visited) 


     
graph={
    0: [1,2,3],
    1: [0,3],
    2:[1,0,0,1],
    3:[1,1,1,1],

}
print('\nDFS using adjacency list:')
dfs_adj_list(graph,0)
