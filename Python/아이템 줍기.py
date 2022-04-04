'''
===================================================================================================================================
문제
===================================================================================================================================
교점에 별 만들기 ☆☆
===================================================================================================================================
Log
===================================================================================================================================
2022-04-04 MON : 문제 파악
                 그래프는 구현했음
                 -> 갈 수 있는 길을 어떻게 분류할지 고민해야함
                 갈 수 있는 길을 분류하다가 중간에 길이 끊겨버리는 문제
                 갈 수 있는 길 분류 완료
                 BFS로 완전탐색 -> 최단 거리를 찾는 문제
                 도형끼리 붙여놨을 때 중간에 빈 공간이 생기면 어떻게 해야하는가
===================================================================================================================================
'''

'''
Algorithm
1. 각 좌표마다 갈 수 있는 경로를 GRAPH로 구현
    -> 모든 좌표를 검사하면서 상자의 좌표가 겹치는 횟수 저장
2. graph에서 상자 내의 좌표는 모두 0으로 설정
3. dfs이용해 완전탐색

'''

from collections import deque
def bfs(x, y, visited, graph, item):
    
    # 이동 방향 : 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        # 큐에서 꺼내기
        x, y = queue.popleft()
        print('x:', x, 'y:', y)
        temp = []
        for dx, dy in directions:
            
            nx = x + dx
            ny = y + dy
            
            # 범위를 벗어나면 continue
            if nx < 0 or nx > MAX-1 or ny < 0 or ny > MAX-1:
                continue
            
            # 이미 방문한 적 있거나 graph의 값이 0이면 continue
            if visited[nx][ny] > -1 or graph[nx][ny] == 0:
                continue
            
            temp.append((nx, ny))
        
        # 갈 수 있는 길이 여러 칸이면 graph에서 값이 가장 큰 쪽으로 이동
        # print(temp)
        if len(temp) > 1:
            temp.sort(key = lambda x: -graph[x[0]][x[1]])
            temp = temp[:1]
        # 인접 칸 큐에 추가
        queue.extend(temp)
        # print(queue)
        # print(temp)
        # print()
        # 방문 기록
        visited[temp[0][0]][temp[0][1]] = visited[x][y] + 1

        # 마지막 칸이면 return
        if (nx, ny) == item:
            return True

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = []
    
    # graph 구현
    graph = []
    global MAX
    MAX = 11 # 나중에 51로 변경하기
    for i in range(MAX):
        temp = []
        for j in range(MAX):
            temp.append(0)
        graph.append(temp)
    
    # 모든 좌표를 검사하면서 상자의 좌표가 겹치는 횟수 저장
    for x1, y1, x2, y2 in rectangle:

        # 가로 방향 검사
        for x in range(x1, x2+1):
            graph[MAX-y1-1][x] += 1
            graph[MAX-y2-1][x] += 1

        # 세로 방향 검사
        for y in range(y2-1, y1, -1):
            graph[MAX-y-1][x1] += 1
            graph[MAX-y-1][x2] += 1
    
    # 상자 내의 좌표 모두 0으로 변경
    for x1, y1, x2, y2 in rectangle:
        for y in range(y2-1, y1, -1):
            for x in range(x1+1, x2):
                graph[MAX-y-1][x] = 0
    for i in graph:
        print(i)
    # bfs로 완전탐색
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    temp = []
    # 시작 칸의 상, 하, 좌, 우 중 갈 수 있는 길 모두 찾기
    for dx, dy in dir:
        nx = MAX-characterY-1 + dx
        ny = characterX + dy
        if graph[nx][ny] != 0:
            temp.append((nx, ny))

    # 갈 수 있는 길이 3개 이상이면 graph의 값이 큰 2군데 길로 출발
    if len(temp) > 2:
        temp.sort(key = lambda x: -graph[x[0]][x[1]])
        temp = temp[2:]
    
    # 양쪽 길로 모두 bfs 수행
    for x, y in temp:
        visited = [[-1 for _ in range(MAX)] for _ in range(MAX)]
        visited[MAX-characterY-1][characterX] = 0
        bfs(x, y, visited, graph, (MAX-itemY-1, itemX))
        answer.append(visited[MAX-itemY-1][itemX])
    return min(answer)

# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17 O
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11
# print(solution([[1,1,5,7]], 1, 1, 4, 7)) # 9 O
# print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)) # 15 O
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)) # 10