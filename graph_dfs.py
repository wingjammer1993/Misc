visited = []
sort_list = []


def dfs_recursive(i_graph, i_start):
    visited.append(i_start)
    print(visited)
    for vertex in i_graph[i_start]:
        if vertex not in visited:
            dfs_recursive(i_graph, vertex)
    sort_list.append(i_start)


def dfs_complete(i_graph, i_start):

    dfs_recursive(i_graph, i_start)
    for vertex in i_graph:
        if vertex not in visited:
            dfs_recursive(i_graph, vertex)
    print(visited)
    print(sort_list)




if __name__ == "__main__":
    graph = {'A': {'C'},
             'B': {'A', 'C'},
             'C': {'D', 'E'},
             'D': {'F', 'E'},
             'E': {'F'},
             'F': {}}

    dfs_complete(graph, 'A')

