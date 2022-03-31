'''
===================================================================================================================================
문제
===================================================================================================================================
모음 사전 ☆☆
===================================================================================================================================
Log
===================================================================================================================================
2022-04-01 TUE : 문제 파악
                 문제 해결
===================================================================================================================================
'''

'''
Algorithm
Stack 이용
1. stack의 길이가 5가 아니면 현재 index의 문자 append
2. stack의 길이가 5이면 마지막 글자 확인
2.1. stack의 마지막 글자가 U가 아니면 POP하고 다음 INDEX의 문자 APPEND
2-2. stack의 마지막 글자가 U이면 마지막에 U가 연속으로 들어있는 개수만는 POP하고 다음 INDEX의 문자 APPEND
3. ANSWER 1씩 증가
'''
def solution(word):
    answer = 1
    stack = ['A']
    index = 0 # 알파벳의 index
    alphabet = ['A', 'E', 'I', 'O', 'U']
    count = 0 # U를 몇 번 만났는지 count
    while stack:
        # A를 찾는 경우 while 돌지 않고 바로 출력
        if word == 'A':
            break
            
        # 길이가 5가 아니면 현재 index의 문자 append
        if len(stack) < 5:
            stack.append(alphabet[index])
            answer += 1

        else: # 길이가 5이면 마지막 글자 확인
            # stack의 마지막 원소가 U가 아니면 다음 INDEX의 alphabet append
            if stack[-1] != 'U':
                stack.pop()
                # 다음 index로 변경
                index = (index+1)%5
            else: # stack의 마지막 원소가 U이면 U가 연속으로 들어있는 개수만큼 POP후 다음 원소 APPEND
                # 끝에서부터 U가 연속으로 몇 개 있는지 확인
                count = 0
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == 'U':
                        count += 1
                    else:
                        break
                
                # U가 연속으로 있는 개수만큼 POP
                for _ in range(count):
                    stack.pop()
                # stack의 변경될 자리의 alphabet의 다음 index 저장
                index = (alphabet.index(stack[-1])+1)%5
                # stack의 변경되어야할 자리의 alphabet pop하고
                stack.pop()
                # 미리 저장해두었던 index의 alphabet으로 변경하고
                stack.append(alphabet[index])
                # index를 0으로 설정
                index = 0
                answer += 1
        
        # 현재 stack의 값이 word와 같아지면 break
        if ''.join(stack) == word:
            break
        
    return answer

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189