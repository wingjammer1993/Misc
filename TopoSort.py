visited = []
sort_list = []


def topo_sort(i_graph, i_start):
    visited.append(i_start)
    for vertex in i_graph[i_start]:
        if vertex[0] not in visited:
            topo_sort(i_graph, vertex[0])
    sort_list.append(i_start)


def longest(i_graph, topo_sorted):
    dict_ver = {}
    for vertex in topo_sorted:
        if vertex not in dict_ver:
            dict_ver[vertex] = 0
        for vert in i_graph[vertex]:
            if vert[0] in dict_ver:
                weight = dict_ver[vert[0]]
            else:
                weight = 0
            if weight < vert[1] + dict_ver[vertex]:
                dict_ver[vert[0]] = vert[1] + dict_ver[vertex]
    print(dict_ver)





if __name__ == "__main__":
    graph = {'A': {('B', 5), ('C', 2)},
             'B': {('D', 6), ('E', 3)},
             'C': {('D', 3), ('E', 4), ('F', 7)},
             'D': {('E', 8), ('F', 7)},
             'E': {},
             'F': {}}

    topo_sort(graph, 'A')
    print(list(reversed(sort_list)))
    longest(graph, list(reversed(sort_list)))



