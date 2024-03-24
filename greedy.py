graph = {
  'A' : [{'B': 1, 'C': 1}, 8],
  'B' : [{'D': 2, 'C': 2, 'E': 1}, 2],
  'C' : [{'B': 2, 'F': 2}, 1],
  'D' : [{'F': 0}, 4],
  'E' : [{'F': 3}, 2],
  'F' : [{}, 0]
}

def greedy(graph, start, end):#implements bfs
	if (start == end):
		return []
	visited = []
	queue = [start]
	while (queue):
		node = queue.pop()
		if node in visited:
			continue
		if node == end:
			return visited
		visited.append(node)
		queue.extend(sorted(graph[node][0], key=lambda x : graph[x][1]))

print(greedy(graph, 'A', 'F'))