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
===================================================================================================================================
'''

'''
Algorithm
1. 각 좌표마다 갈 수 있는 경로를 GRAPH로 구현
    -> 모든 좌표를 검사하면서 상자의 좌표가 겹치는 횟수 저장
2. graph에서 2가 3개 이상 있는 경우 처음 2가 나오는 곳과 마지막으로 2가 나오는 곳 사이의 값들은 0으로 변경
'''

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # graph 구현
    graph = []
    MAX = 11 # 나중에 51로 변경하기
    for i in range(MAX):
        temp = []
        for j in range(MAX):
            temp.append(0)
        graph.append(temp)
    
    # 모든 좌표를 검사하면서 상자의 좌표가 2번 이하로 나오면 True, 3번 이상 나오면 False 저장
    for x1, y1, x2, y2 in rectangle:
        # x1, y1, x2, y2 = rect_info
        # print(x1, y1, x2, y2)
        # 가로 방향 검사
        for x in range(x1, x2+1):
            # print('(', x, y1, '), (', x, y2, ')')
            # graph[x][y1] += 1
            # graph[x][y2] += 1
            graph[MAX-y1-1][x] += 1
            graph[MAX-y2-1][x] += 1
        # print()
        # 세로 방향 검사
        for y in range(y2-1, y1, -1):
            # print('(', x1, y, '), (', x2, y, ')')
            # graph[x1][y] += 1
            # graph[x2][y] += 1
            graph[MAX-y-1][x1] += 1
            graph[MAX-y-1][x2] += 1
        # print()
    for i in graph:
        print(i)
        
    # 갈 수 있는 길 분류
    for x in range(MAX):
        
        # 2가 3개 이상인 경우 첫 번째 2의 위치와 마지막 2의 위치 사이의 값들을 모두 0으로 변경
        # 가로줄 확인
        temp = ''.join(map(str, graph[x]))
        if 2 in graph[x] and temp.count('2') > 1:
            for y in range(temp.find('2')+1, temp.rfind('2')):
                print('x1:', x, 'y1:', y)
                graph[x][y] = 0
        # for i in graph:
        #     print(i)
        # 세로줄 확인
        count = 0
        print('start:', count)
        temp = ''
        for y in range(MAX):
            if graph[y][x] == 2:
                count += 1
            temp += str(graph[y][x])
        print('end:', count)
        if count > 1:
            print(temp)
            for y in range(temp.find('2')+1, temp.rfind('2')):
                print('x:', x, 'y:', y)
                graph[y][x] = 0

    for i in graph:
        print(i)
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11
# print(solution([[1,1,5,7]], 1, 1, 4, 7)) # 9
# print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)) # 15
# print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)) # 10