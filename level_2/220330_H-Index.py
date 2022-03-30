'''
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, 
h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 
h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
'''

def solution(citations):
    h_idx = [] # 인용횟수와 인용횟수 이상의 논문 개수를 함께 담을 리스트
    for i in range(len(citations)+1): # 인용 회수를 1씩 늘려가면서 반복
        h = len([x for x in citations if x>=i]) # 인용 회수 i 이상인 논문의 개수
        h_idx.append([i,h]) # 두 개를 하나의 리스트로 만들어서 h_idx에 추가
        
    for i in h_idx: 
        if i[0]>i[1]: # 만약 인용 횟수가 인용 횟수된 논문의 개수보다 많다면
            return i[0]-1 # 인용 회수-1을 반환
        elif i[0] == i[1]: # 같다면
            return i[0] # 인용된 회수 반환
        
        

citations = [3,0,6,1,5]
citations = [10,100]
# citations = [6,6,6,6,6,6]
# citations = [2,2,2]
citations = [0,0,0,0,0]
print(solution(citations)) 