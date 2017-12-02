
def bfs(i_graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex in i_graph:
                queue.extend(graph[vertex] - visited)
    return visited


if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
             'B': set(['C', 'D']),
             'C': set(['A'])}

    traversal = bfs(graph, 'A')
    print(traversal)
