'''
정수 n, left, right가 주어집니다. 
다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
정수 n, left, right가 매개변수로 주어집니다. 
주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.
'''

# 런타임 에러 코드(시간초과)
def solution(n, left, right):
    result = [] # 결과 배열
    for i in range(n): # 행 반복
        arr = []
        for j in range(n): # 열 반복
            arr.append(max(i,j)+1) # 행과 열 중에서 큰 수에 1을 더해서 행렬에 추가
        result.append(arr) # 행을 결과 배열에 추가

    return sum(result,[])[left:right+1] # 중복 배열? 합쳐서 슬라이싱 하기

##############################################################################################3

# 정답 코드
# 필요한 부분만 배열에 추가하는 방식
def solution(n, left, right):
    '''left 부터 right+1까지 반복
    만약 위치의 숫자를 배열 길이로 나누었을 때
    몫과 나머지 중 큰 수에 +1을 하여 배열에 추가
    '''
    return [(i//n)+1 if i//n>i%n else (i%n)+1 for i in range(left,right+1)]

print(solution(4,7,14))