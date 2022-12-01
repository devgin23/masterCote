# 주의 할 것!!! 
# visited = [[False] * M ]* N 이라고 해서 행들이 모두 같은 참조값을 가지게 코딩했었다.
# visited = [[False] * M for _ in range(N)]

N, M = map(int,input().split())
tool = []
for i in range(N):
    tool.append(list(map(int,list(input()))))
for o in tool:
    print(o)
# visited = [[False] * M] * N
visited = [[False] * M for _ in range(N)]
for p in visited:
    print(p)

def searchNear(r,c,visited,count,tool):
    flagCount = True
    vec = [[-1,0],[1,0],[0,-1],[0,1]]
    for k in range(len(vec)):
        newR = r+vec[k][0]
        newC = c+vec[k][1]
        if 0 <= newR < N and 0<= newC < M :
            if not visited[newR][newC] :
                if tool[newR][newC] == 0 :
                    visited[newR][newC] = True
                    flagCount = False
    if flagCount : count+=1
count = 0
for i in range(N):
    for j in range(M):
        if tool[i][j] == 0:
            print(i,j)
            print("visited[][] = 0 :",i,j)
            visited[i][j] = True 
            searchNear(i,j,visited,count,tool)
            for u in visited:
                print(u)
print(count)