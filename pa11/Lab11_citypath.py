import heapq

n = int(input())

# graph 노드 번호를 0부터 시작하도록 설정하고 인접 리스트 생성
graph_arr = []

for i in range(n):
    tmp_arr = list(map(int, input().split()))[1:-1]
    tmp_arr = list(map(lambda x:x-1, tmp_arr))
    graph_arr.append(tmp_arr)

# 그래프의 (차수-1)을 degree에 저장
degree = list(map(lambda x:len(x)-1, graph_arr))

# 한 노드에서 다른 노드들까지의 최단거리를 찾는 dijkstra 알고리즘 적용
# start 노드에서부터 각 노드까지 최단거리 찾음
def dijkstra(graph, start):
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        d, v = heapq.heappop(queue)
        # 인접리스트의 다음 노드들을 확인
        for next_v in graph[v]:
            # 현재 노드 v에서 다음 노드 next_v 까지의 거리는 1 + degree[next_v]이므로,
            # 현재노드까지의 거리 + 1 + degree[next_v]와, degree[next_v] 중에 최솟값 갱신하고, heap에 push
            if distances[next_v] > distances[v] + 1 + degree[next_v]:
                distances[next_v] = distances[v] + 1 +degree[next_v]
                heapq.heappush(queue, [distances[next_v], next_v])
    # 마지막 노드의 차수까지 더했으므로, 마지막 노드의 차수를 결과값에서 빼준다.
    for i in range(n):
        if i != start:
            distances[i] -= degree[i]
    return distances

# 모든 노드에서 dijkstra 알고리즘을 적용하여 나온 거리 리스트 중에 최댓값을 구한다.
arr = []
for i in range(len(graph_arr)):
    arr.append(max(dijkstra(graph_arr, i)))

answer = max(arr)
print(answer)


