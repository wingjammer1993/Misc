visited = []


def dfs_recursive(i_graph, i_start):
    visited.append(i_start)
    print(visited)
    for vertex in i_graph[i_start]:
        if vertex not in visited:
            dfs_recursive(i_graph, vertex)


if __name__ == "__main__":
    graph = {'A': {'B', 'C'},
             'B': {'A', 'D', 'E'},
             'C': {'A', 'F'},
             'D': {'B'},
             'E': {'B', 'F'},
             'F': {'C', 'E'}}

    dfs_recursive(graph, 'A')