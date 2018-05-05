listed = []
try:
	while True:
		inp = raw_input()
		if inp != "":
			listed.append(inp)
		else:
			break
except EOFError:
	pass

index = 0
graphs = []
transpose = []
while index < len(listed):
	m = listed[index][0]
	n = listed[index][-1]
	graph_case = {}
	graph_transpose = {}
	index += 1
	for j in range(0, int(n)):
		if listed[index][0] in graph_case:
			graph_case[listed[index][0]].append(listed[index][-1])
			if listed[index][-1] not in graph_case:
				graph_case[listed[index][-1]] = []
		else:
			graph_case[listed[index][0]] = [listed[index][-1]]
			if listed[index][-1] not in graph_case:
				graph_case[listed[index][-1]] = []

		if listed[index][-1] in graph_transpose:
			graph_transpose[listed[index][-1]].append(listed[index][0])
			if listed[index][0] not in graph_transpose:
				graph_transpose[listed[index][0]] = []
		else:
			graph_transpose[listed[index][-1]] = [listed[index][0]]
			if listed[index][0] not in graph_transpose:
				graph_transpose[listed[index][0]] = []

		index += 1
	graphs.append(graph_case)
	transpose.append(graph_transpose)

visited = []


def dfs_recursive(i_graph, i_start):
	visited.append(i_start)
	for vertex in i_graph[i_start]:
		if vertex not in visited:
			dfs_recursive(i_graph, vertex)


straight_connected = []
straight_disconnected = []


for i in graphs:
	list_1 = list(i.keys())
	dfs_recursive(i, list_1[0])
	if set(list_1) == set(visited):
		straight_connected.append(graphs.index(i))
	else:
		straight_disconnected.append(graphs.index(i))
	visited = []

transpose_connected = []
transpose_disconnected = []

for k in transpose:
	list_1 = list(k.keys())
	dfs_recursive(k, list_1[0])
	if set(list_1) == set(visited):
		transpose_connected.append(transpose.index(k))
	else:
		transpose_disconnected.append(transpose.index(k))
	visited = []


