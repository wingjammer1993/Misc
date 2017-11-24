visited = []
sort_list = []


def topo_sort(i_graph, i_start):
    visited.append(i_start)
    for vertex in i_graph[i_start]:
        if vertex not in visited:
            topo_sort(i_graph, vertex)
    sort_list.append(i_start)


if __name__ == "__main__":
    graph = {'A': {'B', 'C'},
             'B': {'D', 'E'},
             'C': {'D', 'E', 'F'},
             'D': {'E', 'F'},
             'E': {'F'},
             'F': {}}

    topo_sort(graph, 'A')
    print(list(reversed(sort_list)))

