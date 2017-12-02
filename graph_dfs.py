visited = []
sort_list = []
rec_stack = []

def dfs_recursive(i_graph, i_start):
    visited.append(i_start)
    rec_stack.append(i_start)
    #print(visited)
    for vertex in i_graph[i_start]:
        if vertex not in visited:
            dfs_recursive(i_graph, vertex)
        if vertex in rec_stack:
            print('cycle detected')
    rec_stack.remove(i_start)
    #print(rec_stack)
    sort_list.append(i_start)


def dfs_complete(i_graph, i_start):

    dfs_recursive(i_graph, i_start)
    for vertex in i_graph:
        if vertex not in visited:
            dfs_recursive(i_graph, vertex)
    #print(visited)
    #print(sort_list)


if __name__ == "__main__":
    graph = {'A': {'B'},
             'B': {'D'},
             'C': {'E', 'A'},
             'D': {'C', 'F', 'E'},
             'E': {'F'},
             'F': {}}

    dfs_complete(graph, 'A')
    print(sort_list)

