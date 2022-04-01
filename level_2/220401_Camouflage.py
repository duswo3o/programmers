
# 1번 tc에서 시간초과
'''from itertools import combinations

def solution(clothes):
    key = list(set([i[1] for i in clothes])) 
    clothes_dict = {}
    
    for i in key:
        clothes_dict[i] = []
        
    for i in clothes:
        clothes_dict[i[1]].append(i[0])
        
    number = [len(clothes_dict[i]) for i in key]
    
    if len(number)==1: # 만약 의상 종류가 한 가지만 있다면
        return number[0] # 하나씩만 입는 경우 반환
    elif len(number) == 2: # 의상의 종류가 두 가지라면
        return sum(number)+(number[0]*number[1]) # 한 가지씩 입는 경우 + 두 가지를 조합해서 입는 경우
    else: # 3가지 이상인 경우
        comb = [list(combinations(number,i)) for i in range(2,len(number)+1)] # 조합 가능한 의상의 리스트
        total = 0 
        for i in range(len(comb)):
            for j in range(len(comb[i])):
                mul = 1
                for s in comb[i][j]: # 각각의 튜플을 꺼내주어 곱셈계산
                    mul *= s
                total+=mul # 전체 조합 가능한 의상의 개수
        return total+sum(number) # 한 가지만 입는 경우 + 조합한 의상을 입는 경우 반환'''
        
def solution(clothes):
    key = list(set([i[1] for i in clothes])) # 의상종류를 중복 없이 리스트로 만들기
    clothes_dict = {}
    
    for i in key: 
        clothes_dict[i] = [] # 의상종류를 키 값으로 딕셔너리 생성
        
    for i in clothes: 
        clothes_dict[i[1]].append(i[0]) # 의상종류가 같은 의상끼리 리스트로 묶어주기
        
    number = [len(clothes_dict[i])+1 for i in key] # 의상종류의 개수에 +1을 해서 리스트에 저장
    # +1을 하는 이유는 한 가지만 입는 경우를 세어주기 위함
    
    total = 1 # 조합 가능한 의상의 종류 초기화
    for i in number:
        total*=i # 조합 가능한 의상을 계산
        
    return total-1 # 반드시 하나는 선택해야하므로 (아무것도 입지 않은 경우 제외)

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))

# a = [[(3, 2), (3, 1), (2, 1)], [(3, 2, 1)]]
