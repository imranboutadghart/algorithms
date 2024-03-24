graph = {
  "S": ["B", "C", "D"],
  "B": ["E"],
  "D": [],
  "E": ["F", "G"],
  "F": [],
  "G": [],
  "C": ["G"],  
}

def bfs(graph, start, end):
	if start == end:
		return [start], []
	visited = []
	explored = []
	parent_path = {}
	queue = [start]
	while queue:
		node = queue.pop(0)
		if node not in visited:
			visited.append(node)
			if node == end:
				path = [end]
				while (node != start):
					path.append(parent_path[node])
					node = parent_path[node]
				return path[::-1], visited
			queue.extend(graph[node])
			for child in graph[node]:
				if child not in explored:
					parent_path[child] = node
				explored.extend(child)
	return [], visited

def dfs(graph, start, end):
	if start == end:
		return [start], []
	visited = []
	explored = []
	parent_path = {}
	stack = [start]
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			if node == end:
				path = [end]
				while (node != start):
					path.append(parent_path[node])
					node = parent_path[node]
				return path[::-1], visited
			stack.extend(graph[node])
			for child in graph[node]:
				if child not in explored:
					parent_path[child] = node
				explored.extend(child)
	return visited


print("bfs : ", end="")
path, visited = bfs(graph, "S", "G")
print(path)
print("visited : ", end="")
print(visited)


print("\n\ndfs : ", end="")
path, visited = dfs(graph, "S", "G")
print(path)
print("visited : ", end="")
print(visited)