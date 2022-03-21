'''
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 
몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
'''


def solution(progresses, speeds):
    
    # 남은 작업 량
    rest = []
    for i in range(len(progresses)):
        rest.append(100-progresses[i])
    
    # 남은 작업을 수행하는데 걸리는 시간    
    take = []
    for i in range(len(rest)):
        if rest[i]%speeds[i] == 0: # 남은 작업 량과 작업 속도가 나누어 떨어질 때
            take.append(rest[i]//speeds[i])
        else: # 남은 작업량과 작업 속도가 나누어떨어지지 않을 때
            take.append(rest[i]//speeds[i]+1) # 몫 + 1
    
    # 한 번에 배포할 수 있는 개수    
    release = []
    # 초기값 설정
    r = take[0] # 작업에 걸린 시간
    t = 1 # 배포할 수 있는 개수
    for i in range(1,len(take)):
        if r>=take[i]: # 다음 숫자보다 크거나 같다면ㄴ
            t += 1 # 배포량 +1
        else: # 다음 숫자가 더 크다면
            release.append(t) # 이전 배포 가능한 개수를 리스트에 추가하고
            r = take[i] # 작업에 걸린 시간 초기화
            t = 1 # 배포 가능한 개수 초기화
    release.append(t) # 최종 배포 가능 개수 리스트에 추가
        
    return release

progresses = [2,2,1,2]
speeds = [1,1,1,1]

print(solution(progresses, speeds))