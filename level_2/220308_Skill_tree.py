'''
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 
썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 
라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 
따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 
썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 
가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.
'''

def solution(skill, skill_trees):
    idx = [] # 인덱스를 저장할 리스트 생성
    for i in skill_trees: # 모든 스킬트리에 대해서
        order = [] # 순서를 저장할 리스트 초기화
        for j in skill: 
            if j in i: # 스킬이 스킬트리에 있다면
                order.append(i.index(j)) # 스킬의 인덱스를 리스트에 추가
            else: # 스킬이 스킬트리에 없다면
                order.append(len(i)+1) # 스킬트리의 길이+1을 리스트에 추가
        idx.append(order) #
    
    answer = 0 # 가능한 스킬트리의 개수
    for i in idx: # 인덱스를 저장한 리스트에서
        if i == sorted(i): # 추출한 인덱스의 순서와 정렬한 인덱스의 순서가 같다면
              answer+=1  # 가능한 스킬트리에 추가
    
    return answer

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))