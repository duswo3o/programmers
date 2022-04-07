'''
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 
해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 
각 로직에 대한 성능 측정을 수행하였는데, 
제이지가 작성한 부분 중 데이터베이스에서 
게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 
제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 
캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, 
DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
'''

from collections import deque # deque 모듈 불러오기

def solution(cachesize, cities):
    cache = deque([]) # 캐시의 내용을 deque로 저장
    time = 0 # 실행시간
    
    if cachesize == 0: # 만약 캐시의 크기가 0이라면
        return len(cities)*5 # (도시이름 배열의 크기)*5
    
    else: # 캐시의 크기가 1 이상이라면
        for i in range(len(cities)): # 도시이름 배열의 크기만큼 반복문 실행
            cities[i]=cities[i].lower() # 대소문자의 구분이 없기때문에 수정
        
        for i in cities:
            if len(cache)<cachesize: # 현재 캐시 데이터가 캐시 크기보다 작을때
                if i in cache: # 현재 찾는 도시가 캐시에 있다면
                    # 도시를 최근 검색으로 업데이트
                    del cache[cache.index(i)] 
                    cache.append(i)
                    time += 1 # 캐시 안에 있기 때문에 걸린시간은 +1
                else: # 현재 찾는 도시가 캐시에 없다면
                    cache.append(i) # 도시를 캐시에 추가
                    time += 5 # 캐시 안어 없으므로 걸린시간 +5
            else: # 만약 현대 캐시가 꽉차있을때
                if i in cache: # 찾는 도시가 캐시 안에 있다면
                    # 도시를 최근 검색으로 업데이트
                    del cache[cache.index(i)]
                    cache.append(i)
                    time += 1 # 걸린시간 +1
                else: # 찾는 도시가 캐시 안에 없다면
                    cache.popleft() # 가장 오랫동안 참조되지 않은 도시 제거
                    cache.append(i) # 찾는 도시 캐시에 추가
                    time += 5 # 걸린시간 +5
                
    return time

cachesize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", 
          "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", 
          "Seoul", "Jeju", "Pangyo", "Seoul"]

cities  = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", 
           "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", 
          "Rome", "Paris", "Jeju", "NewYork", "Rome"]

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

cities = ["SEOUL", "SEOUL", "SEOUL"]

print(solution(cachesize,cities))