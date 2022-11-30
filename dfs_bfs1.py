N, M = map(int,input().split())
tool = []
for i in range(N):
    tool.append(list(map(int,list(input()))))
print(tool)
visited = [[False] * M] * N

def searchNear(r,c,visited):
    vec = [[-1,-1],[-1,1],[1,-1],[1,1]]
    for i in range(len(vec)):
        newR = r+vec[i][0]
        newC = c+vec[i][1]
        if 0 <= newR < N and 0<= newC < M :
            if not visited[newR][newC] :
                visited[newR][newC] = True
                for i in visited:
                    print(i)
count = 0
for i in range(N):
    for j in range(M):
        if tool[i][j] == 0:
            if not visited[i][j]:
                count += 1
                visited[i][j] = True
                searchNear(i,j,visited)
for i in visited:
    print(i)
print(count)