'''짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 
먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 
그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 
이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.
'''

# 효율성이랑 정확성이랑 조금씩 틀림
'''def solution(s):
    pair = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn',
            'oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    
    for i in pair:
        if i in s:
            s = s.replace(i,'')
            print(s)
        
    return 1 if len(s) == 0 else 0'''

# 정확성은 통과했지만 효율성에서 하나빼고 다 틀림
'''def solution(s):
    pair = {'a':'aa','b':'bb','c':'cc','d':'dd','e':'ee','f':'ff','g':'gg','h':'hh','i':'ii',
            'j':'jj','k':'kk','l':'ll','m':'mm','n':'nn','o':'oo','p':'pp','q':'qq','r':'rr',
            's':'ss','t':'tt','u':'uu','v':'vv', 'w':'ww','x':'xx','y':'yy','z':'zz'}
    
    for i in s:
        if pair[i] in s:
            s = s.replace(pair[i],'')
            print(s)
            
    return 1 if len(s) == 0 else 0'''
    

# 스택을 이용한 풀이
def solution(s):
    S = [] # 문자열을 담을 리스트(스택)
    
    # 문자열을 차례로 하나씩 담기
    for i in s: 
        if len(S)==0: # 만약 리스트가 비어있으면
            S.append(i) # 리스트에 문자 추가
        else:
            if S[-1] == i: # 만약 추가할 문자가 마지막 문자와 같다면
                S.pop() # 마지막 문자 제거
            else: # 추가할 문자와 마지막 문자가 다르면
                S.append(i) # 리스트에 문자 추가
                
    # 문자열을 담을 리스트가 비어있으면 1 출력 그렇지 않으면 0 출력            
    return 1 if len(S) == 0 else 0

s = 'abbcdaadca'

print(solution(s))