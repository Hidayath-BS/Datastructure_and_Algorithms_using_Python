import heapq
def dijkstra(graph, start):
    dist = {node:float('inf') for node in graph}
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        for neighbour, weight in graph[node]:
            new_dist = curr_dist + weight

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbour))
    return dist

graph ={
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5)],
    3:[(4,3)],
    4:[]
}

start_node = 0
shortest_path = dijkstra(graph, start_node)
print("shortest distance from node", start_node)
for node, dist in shortest_path.items():
    print(f"Node {node} : {dist}")