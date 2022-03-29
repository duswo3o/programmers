'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
'''
# 리스트에서 pop(0)을 사용하면 시간 복잡도가 O(n)인데 그냥 pop()을 하면 시간복잡도가 O(1)임
# 그래서 deque에서 popleft() 함수를 사용해서 효율성을 높임
from collections import deque # deque 모듈 불러오기
def solution(prices):
    prices = deque(prices) # 주식가격 리스트를 deque로 변경
    answer = [] # 가격이 떨어지지 않는 기간을 담을 리스트(정답 리스트)
    while len(prices)!=0: # 리스트의 길이가 0이 아닐때까지
        count = 0 # 떨어지지 않는 기간
        a = prices.popleft() # 첫 번째 원소를 기준으로
        # for i in prices가 for i in range(len(prices))보다 효율성이 좋음
        for i in prices: # 뒤의 원소들과의 가격 비교
            if a > i: # 만약 가격이 하락한다면
                count+=1 # 1초는 유지하는것으로 보기때문에
                break # 다음 반복문 진행
            else:
                count+=1 # 가격이 떨어지지 않으면 1초 추가
        answer.append(count) # 떨어지지 않는 기간을 리스트에 추가
            
    return answer

prices = [1,2,3,2,3]
print(solution(prices))