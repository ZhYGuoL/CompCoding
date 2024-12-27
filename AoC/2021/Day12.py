# data = open('Day12Input.txt').read().splitlines()


# def dfs(u):
# 	global res
# 	if u == 'end':
# 		res += 1
	
# 	visited[u] = True
# 	for v in graph[u]:
# 		if not visited[v] or v.isupper():
# 			dfs(v)
	
# 	visited[u] = False

# graph = {}

# for l in data:
# 	u, v = l.split('-')
# 	if u not in graph:
# 		graph[u] = []
# 	if v not in graph:
# 		graph[v] = []
# 	graph[u].append(v)
# 	graph[v].append(u)

# visited = {i: False for i in graph.keys()}
# visited['start'] = True
# res = 0
# dfs('start')

# print(res)



from collections import deque, defaultdict

data = open('Day12Input.txt').read().splitlines()

caves = defaultdict(set)
for line in data:
    x, y = line.split("-")
    caves[x].add(y)
    caves[y].add(x)


def get_neighbors_a(here, visited):
    return [c for c in caves[here] if c.isupper() or c not in visited]


def get_neighbors_b(here, visited):
    if any(v > 1 for k, v in visited.items() if not k.isupper()):
        # we've already visited a small cave twice
        return get_neighbors_a(here, visited)
    return [n for n in caves[here] if n != "start"]


def n_paths(part):
    get_neighbors = get_neighbors_a if part == "a" else get_neighbors_b
    result = 0
    q = deque([(["start"], {"start": 1})])
    while q:
        path, visited = q.pop()
        here = path[-1]
        if here == "end":
            result += 1
            continue
        neighbors = get_neighbors(here, visited)
        q.extend([(path + [n], {**visited, n: visited.get(n, 0) + 1}) for n in neighbors])
    return result


print("part a:", n_paths("a"))
print("part b:", n_paths("b"))