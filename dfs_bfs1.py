N, M = map(int,input().split())
tool = []
for i in range(N):
    tool.append(list(map(int,list(input()))))
for i in tool:
    print(i)
visited = [[False] * M] * N

def searchNear(r,c,visited):
    vec = [[-1,-1],[-1,1],[1,-1],[1,1]]
    for i in range(len(vec)):
        newR = r+vec[i][0]
        newC = c+vec[i][1]
        if 0 <= newR < N and 0<= newC < M :
            if not visited[newR][newC] :
                visited[newR][newC] = True
count = 0
for i in range(N):
    for j in range(M):
        if tool[i][j] == 0:
            if not visited[i][j]:
                count += 1
                visited[i][j] = True
                print(i,j)
                for k in visited:
                    print(k)
                searchNear(i,j,visited)
for i in visited:
    print(i)
print(count)