'''
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 
예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 
문자열 s가 올바른 괄호이면 true를 return 하고, 
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
'''

def solution(s):
    parenthesis = [] # 괄호를 담을 리스트
    for i in s:
        parenthesis.append(i) # 리스트에 괄호추가하기
        if len(parenthesis)>1: # 리스트의 길이가 1보다 클 때(2 이상일 때)
            if parenthesis[-1]==')' and parenthesis[-2] =='(': # 리스트의 가장 마지막 원소와 뒤에서 두 번째 원소가 같다면
                parenthesis.pop(-1) # 괄호 제거하기
                parenthesis.pop(-1)
                
    if bool(parenthesis)==True: # 모든 괄호 제거 후에 괄호가 남아있다면 
        return False # False 반환
    else: #그렇지 않으면 
        return True # True 반환
    
print(solution('()()'))