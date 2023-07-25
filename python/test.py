# BFS

from collections import deque

M, N, H = list(map(int, input().split()))

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

dh = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 0, 1, 0]
dx = [0, 0, 0, 1, 0, -1]

queue = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                visited[i][j][k] = True
                queue.append([i, j, k, 0])

while len(queue) != 0:
    h, y, x = queue.popleft()
    for d in range(6):
        nh = h + dh[d]
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M and not visited[nh][ny][nx] and box[nh][ny][nx] == 0:
            