import heapq

N = int(input())
star_list = [tuple(map(float, input().split())) for i in range(N)]
hq = []
heapq.heappush(hq, (0, 0))
result = 0
visited = set()

while hq:
    dist, node = heapq.heappop(hq)
    if node in visited:
        continue
    visited.add(node)
    result += dist
    if len(visited) == N:
        break
    for i in range(N):
        if i != node:
            n_dist = abs(star_list[node][0] - star_list[i][0]) ** 2 + abs(star_list[node][1] - star_list[i][1]) ** 2
            n_dist **= 0.5
            heapq.heappush(hq, (n_dist, i))
            heapq.heappush(hq, (n_dist + dist, i))


print("{:.2f}".format(result))