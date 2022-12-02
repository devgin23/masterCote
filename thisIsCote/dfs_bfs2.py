

# 0이고 방문하지 않았으면 상하좌우를 살펴본다.
# 상하좌우를 살펴보던 중 0이고 방문하지 않은 것이 있으면 상하좌우를 살펴본다.
# 끝날 때까지 한다.

# 그리고 다음 노드로 간다.
N, M = map(int,input().split())
tool = []
for i in range(N):
    tool.append(list(map(int,list(input()))))
visited = [[False] * M for _ in range(N)]


def visit(r,c,tool,visited):
    visited[r][c]==True
    vec = [[-1,0],[1,0],[0,-1],[0,1]]
    for k in range(len(vec)):
        newR = r+vec[k][0]
        newC = c+vec[k][1]
        if 0 <= newR < N and 0<= newC < M :
            if tool[newR][newC]==0 and not visited[newR][newC]:
                visit(newR,newC,tool,visited)
        else: return
count =0
for i in range(N):
    for j in range(M):
        visit(i,j,tool,visited)
        count += 1
print(count)