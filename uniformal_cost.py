graph = {
  'A': {'B': 1, 'C': 1},
  'B': {'D': 2, 'C' : 2, 'E': 1},
  'C': {'B': 2, 'F': 2},
  'D': {'F': 0},
  'E': {'F': 3},
  'F': {}
}

# print("|cp: ", child_parent, "|c: ", child, "|sub: ", subchild, "|cc: ", child_cost, "|sc:", graph[child][subchild],\
# "|total: ", child_cost + graph[child][subchild], "|visited:", visited) ///debugging
def ucs(graph, start, end):
	if start == end:
		return [start], []
	current = start
	visited = {start : [0, None]}
	while (current != end):
		min_val = -1
		target = None
		for child, [child_cost, child_parent] in visited.items():
			for subchild in graph[child]:
				if subchild in visited and visited[subchild][1] == child:
					continue
				if (min_val == -1\
							or graph[child][subchild] + child_cost < min_val)\
						and (subchild not in visited\
		  					or visited[subchild][0] > graph[child][subchild] + child_cost):
					min_val = graph[child][subchild] + child_cost
					target_parent = child
					target = subchild
		if target == None:
			return [], visited
		visited[target] = [min_val, target_parent]
		current = target
	current = end
	path = [current]
	while visited[current][1]:
		path.append(visited[current][1])
		current = visited[current][1]
	return path[::-1], list(visited.keys())

path, visited = ucs(graph, 'A', 'F')
print(path, visited)
