'''
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 
구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 
2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 
구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 
solution 함수를 작성해주세요.'''

from collections import deque

def solution(people, limit):
    answer = 0 # 구출에 필요한 구명보트의 개수
    people = deque(sorted(people, reverse = True)) # 내림차순으로 정렬
    
    # deque를 이용해 양쪽에서 pop할 예정
    while len(people)>2: # 리스트에 최소 두 명이 있어야 오류가 안나기 때문에
        heavy = people.popleft() # 가장 무거운 사람
        light = people.pop() # 가장 가벼운 사람
        if heavy+light>limit: # 가장 무거운 사람과 가장 가벼운 사람의 합이 무게제한을 넘는다면
            people.append(light) # 가장 가벼운 사람은 다시 리스트에 추가
        answer+=1 # 필요한 구명보트의 개수 +1
    
    # 2명 혹은 1명이 남았을 때    
    if sum(people)>limit: # 2명이 남았는데 두 명 몸무게의 합이 무게제한을 넘으면
        return answer+2 # 보트 2개 필요
    else: # 무게제한을 넘지 않으면
        return answer+1 # 보트 1개 필요

people = [40, 50, 60, 90]
limit = 100

print(solution(people, limit))