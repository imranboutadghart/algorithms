graph = {
  'A' : [{'B': 1, 'C': 1}, 5],
  'B' : [{'D': 2, 'C': 2, 'E': 1}, 2],
  'C' : [{'B': 2, 'F': 2}, 1],
  'D' : [{'F': 0}, 4],
  'E' : [{'F': 3}, 2],
  'F' : [{}, 0]
}

# print("|cp: ", child_parent, "|c: ", child, "|sub: ", subchild, "|cc: ", child_cost, "|sc:", graph[child][subchild],\
# "|total: ", child_cost + graph[child][subchild], "|visited:", visited) ///debugging
def ucs(graph, start, end):
	if start == end:
		return [start], []
	current = start
	visited = {start : [graph[start][1], None]}
	while (current != end):
		min_val = -1
		target = None
		for child, [child_cost, child_parent] in visited.items():
			for subchild in graph[child][0]:
				if subchild in visited and visited[subchild][1] == child:
					continue
				if (min_val == -1\
							or graph[child][0][subchild] + graph[subchild][1] + child_cost < min_val)\
						and (subchild not in visited\
		  					or visited[subchild][0] > graph[child][0][subchild] + graph[subchild][1] + child_cost):
					min_val = graph[child][0][subchild] + child_cost + graph[subchild][1]
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
