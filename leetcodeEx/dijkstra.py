import collections
import heapq
import functools

def netWorkDelay(times, N, K)->int:
	graph = collections.defaultdict(list)
	for s, d, w in times:
		graph[s].append((d, w))
	visited = collections.defaultdict(int)
	Q = [(0, K)]
	while Q:
		weight,node = heapq.heappop(Q)
		if not node in visited:
			visited[node] = weight 
			for d, w in graph[node]:
				new_weight = weight + w
				heapq.heappush(Q, (new_weight, d))
	if len(visited) !=  N:
		return -1
	return max(visited.values())
	
times =[[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6,7, 1], [7, 8, 1], [8, 1,1]]
N = 8
K = 3
print(netWorkDelay(times, N, K))
		
		
