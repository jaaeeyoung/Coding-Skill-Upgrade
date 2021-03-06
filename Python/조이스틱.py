'''
===================================================================================================================================
문제
===================================================================================================================================
조이스틱 ☆☆
===================================================================================================================================
문제 설명
===================================================================================================================================
' 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
  ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
  
' 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
    ▲ : 다음 알파벳
    ▼ : 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
    ◀ : 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
    ▶ : 커서를 오른쪽으로 이동

' 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
    - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
    - 조이스틱을 위쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
    - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
    따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
    
' 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
===================================================================================================================================
제한 사항
===================================================================================================================================
' name은 알파벳 대문자로만 이루어져 있습니다.
' name의 길이는 1 이상 20 이하입니다.
===================================================================================================================================
입출력 예
===================================================================================================================================
name        return
"JEROEN"    56
"JAN"       23
===================================================================================================================================
입출력 예 설명
===================================================================================================================================
' 입출력 예 #1
===================================================================================================================================
Log
===================================================================================================================================
2021-11-10-Wed : 문제 파악
                 채점 테스트 3 ~ 5, 7, 8, 11 실패 (런타임 에러) (45.5점)
                 check 자료형 변경 (List > Dict), location 이동 조건 변경
                 -> 채점 테스트 3 ~ 5, 7, 8, 11 실패 (45.5점)
                 location 이동 조건 if와 else 순서 변경
                 -> 채점 테스트 3, 4, 7, 8 실패 (런타임 에러), 테스트 11 실패 (54.5점)
                 location 이동 조건 세분화
                 -> 채점 테스트 3, 4, 7, 8, 11 실패 (런타임 에러) (54.5점)
                 4, 5, 7, 8 실패, 11 실패 (런타임 에러)
                 location 이동 시 마지막 A를 찾는 게 아니라 지금 시점부터 A가 총 몇 개 있는지 찾아야될 것 같음
                 문제 해결
===================================================================================================================================
'''

def solution(name):
    answer = 0
    # 현재 index
    location = 0
    # 각 index의 값을 참조한 적 있는지 확인하기 위한 List (참조했다면 True)
    # name의 원소 중 A는 참조할 필요가 없으므로 A인 index는 미리 True로 설정
    check = {}
    index_ = []
    for i in range(len(name)):
        check[i] = False
        index_.append(i)
        if name[i] == 'A':
            check[i] = True
            index_.pop()

    while True:
        if check[location]:
            location += 1
            answer += 1
            continue
        
        # Z에서 원소까지의 거리가 원소에서 A까지의 거리보다 짧으면
        if ord('Z') - ord(name[location]) < ord(name[location]) - ord('A'):
            # 뒤에서부터 접근
            answer += ord('Z') - ord(name[location]) + 1
        else: # 원소에서 A까지의 거리가 Z에서 원소까지의 거리보다 짧으면
            # 앞에서부터 접근
            answer += ord(name[location]) - ord('A')
        # 접근한 index는 True로 변환
        check[location] = True
        
        # check의 모든 원소가 True이면(모든 원소에 접근했다면) break
        if False not in check.values():
            break
        
        # location 이동
        # 앞으로 진행하는 방식과 거꾸로 진행하는 방식 비교
        # location이 index의 마지막 원소보다 크거나 같은 경우
        if location >= index_[-1]:
            answer += location - index_[-2]
            index_ = index_[:index_.index(location)]
            location = index_[-1]
        # location이 index의 첫 원소보다 작거나 같은 경우
        # index의 다음 원소까지의 거리가 마지막 원소까지의 거리보다 긴 경우
        elif location <= index_[0] and len(name) - index_[-1] + location >= index_[1] - location:
            answer += index_[1] - location
            index_ = index_[index_.index(location) + 1:]
            location = index_[0]
        # location이 index의 첫 원소와 마지막 원소 사이에 있는 경우
        else:
            answer += len(name) - index_[-1] + location
            index_ = index_[:index_.index(location)] + index_[index_.index(location) + 1:]
            location = index_[-1]
            
    return answer

# print(solution("JEROEN")) # 56
# print(solution('JAN')) # 23
# print(solution('JAZ')) # 11
# print(solution('ABAAAA')) # 2
# print(solution('ABABAAAAAAABA')) # 11
# print(solution('ABAAAAAAAAABB')) # 7
# print(solution("AABAAAAAAABBB")) # 11
# print(solution("BBBAAB")) # 9
# print(solution('ZAAAZAAAAAA')) # 6
# print(solution('NNAAAAANNN')) # 70
# print(solution('ZAAAZZZZZZZ')) # 15