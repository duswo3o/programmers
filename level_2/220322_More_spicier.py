'''
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 
Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
'''

# 효율성 실패 코드
'''
def solution(scoville,k):
    scoville.sort()
    times = 0
    while(len(scoville)!=1):
        if scoville[0]>=k:
            break
        else:
            n_scoville = scoville[0]+(scoville[1]*2)
            scoville.pop(0)
            scoville[0] = n_scoville
            scoville.sort()
            times+=1
        
    return times if scoville[0]>=k else -1
'''
#######################################################################################3
import heapq # 힙 모듈 사용

def solution(scoville, k):
    heapq.heapify(scoville) # 기존 리스트를 힙 형태로 변환
    times = 0 # 스코빌 지수 업데이트 횟수
    while(len(scoville)!=1): # 스코빌 리스트의 길이가 1일때까지 반복
        if scoville[0]>=k: # 만약 스코빌 지수가 만족이 되면
            break # 반복문 종료
        else:
            a = heapq.heappop(scoville) # 가장 맵지 않은 음식의 스코빌 지수
            b = heapq.heappop(scoville) # 두 번째로 맵지 않은 음식의 스코빌 지수
            n_scoville = a+(b*2) # 섞은 음식의 스코빌 지수
            heapq.heappush(scoville,n_scoville) # 힙 형태의 리스트에 추가
            times+=1 # 업데이트 횟수 추가
            
    # 업데이트 횟수 반환, 만약 스코빌지수를 k이상으로 만들 수 없다면 -1 반환
    return times if scoville[0]>=k else -1 

scoville = [1,2,3,9,10,12]
k = 7

print(solution(scoville,k))
