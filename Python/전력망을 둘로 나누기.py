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
2022-04-03-SUN : 코드 제출 시 테스트케이스 8~13 실패 (53.8) -> 무슨 문제인지 잘 모르겠음
                 모든 노드를 확인하도록 코드 변경 -> 테스트 2 실패 (92.3)
                 dfs() 탐색할 때 for문 쓰지 않고 첫 번째 덩어리만 확인해 n-count하는 방식으로 두번째 덩어리의 노드 개수 확인하는 방식으로
                 변경
                 dfs() 탐색할 때 super node가 sub node보다 작으면 탐색하지 않도록 변경
                 문제 해결
===================================================================================================================================
'''

'''
Algorithm
1. 인접 노드를 graph에 저장
2. 모든 노드를 끊어가면서 연결된 노드 개수 확인
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
    answer = n
    
    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)

    for super_node in range(1, n+1):
        for sub_node in graph[super_node]:
            # super node가 sub node보다 작으면 앞에서 이미 확인했기 때문에 무시
            if super_node < sub_node:
                continue
            # 현재 노드와 연결되어있는 노드 연결 끊기
            graph[super_node].remove(sub_node)
            graph[sub_node].remove(super_node)
            
            # dfs를 이용해 한 덩어리에 몇 개의 노드가 연결되어있는지 확인
            global count
            count = 0
            if dfs(1, [False for _ in range(n+1)], graph):
                answer = min(answer, max(count - (n-count), (n-count) - count))
                    
            # 연결을 끊었던 노드와 다시 연결
            graph[super_node].insert(0, sub_node)
            graph[sub_node].insert(0, super_node)
            
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # 3
print(solution(4, [[1,2],[2,3],[3,4]])) # 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) # 1
# print(solution(6, [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]])) # 2
# print(solution(3, [[1, 2], [2, 3]])) # 1
# print(solution(2, [[1, 2]])) # 0
# print(solution(4, [[1, 2], [2, 3], [2, 4]])) # 2
# print(solution(5, [[1, 2], [2, 3], [2, 4], [2, 5]])) # 3