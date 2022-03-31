'''
===================================================================================================================================
문제
===================================================================================================================================
최소직사각형 ☆☆
===================================================================================================================================
Log
===================================================================================================================================
2022-04-01 TUE : 문제 파악
                 테스트케이스 3번 틀림 -> node_info 리스트 정렬한 후에 노드를 삭제하는 과정을 무조건 index 0, 1로 하면 안될듯
===================================================================================================================================
'''

'''
Algorithm
1. 인접 노드를 graph에 저장
2. 가장 많이 연결되어있는 노드와 그 다음으로 많은 노드를 끊음
3. dfs를 이용해 한 덩어리당 몇 개의 노드로 구성되어있는지 확인
4. 두 덩어리의 노드차의 최솟값을 반환
'''

def dfs(start, visited, graph):
    global count
    # 이미 방문한 적 있으면 무시
    if visited[start]:
        return False
    
    # 현재 노드 방문 표시
    visited[start] = True
    count += 1
    
    # 인접 노드 방문
    for x in graph[start]:
        if not visited[x]:
            dfs(x, visited, graph)
    return True

def solution(n, wires):
    answer = []
    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    # print(graph)
    
    # 각 노드와 연결되어있는 노드 찾기
    # max_len = 0
    # index = 0
    node_info = []
    for i in range(1, n+1):
        node_info.append((i, len(graph[i])))
    # print(node_info)
    
    # 연결된 노드의 개수가 많은 순서대로 정렬
    node_info.sort(key = lambda x:-x[1])
    print(node_info)
    
    # 가장 많은 노드와 연결되어있는 노드와 그 다음으로 많은 노드와 연결되어 있는 노드를 끊음
    graph[node_info[0][0]].remove(node_info[1][0])
    graph[node_info[1][0]].remove(node_info[0][0])
    
    # dfs를 이용해 덩어리당 노드가 몇 개 있는지 확인
    visited = [False for _ in range(n+1)]
    for x in range(1, n+1):
        global count
        count = 0
        if dfs(x, visited, graph):
            answer.append(count)
    return max(answer[0]-answer[1], answer[1]-answer[0])

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3
print(solution(4, [[1,2],[2,3],[3,4]])) # 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) # 1