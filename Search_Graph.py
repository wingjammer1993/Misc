
class SearchGraph:

    def __init__(self):
        self.path = []

    def search_sequence(self, input_graph, start_vertex, list_label):

        if not list_label:
            self.path.append(start_vertex)
            return

        for child, symbol in input_graph[start_vertex]:
            if symbol == list_label[0]:
                list_label.remove(symbol)
                self.path.append(start_vertex)
                self.search_sequence(input_graph, child, list_label)
                break


if __name__ == "__main__":
    graph = {'A': {('B', 'a'), ('C', 'b')},
             'B': {('D', 'b'), ('C', 'c')},
             'C': {('D', 'a'), ('E', 'd')},
             'D': {('E', 'e')},
             'E': set()}

    s = SearchGraph()
    o = ['c', 'a', 'd']
    s.search_sequence(graph, 'B', o)
    path = s.path
    print(path)

