'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 
solution 함수를 작성해주세요.
'''




# 1차 제출
# 1~6, 11 TC에서 실패
# 반례
#     numbers = [30,3021]
#     모두 0인 경우도 처리해줘야해서 실패

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     m = max([len(j) for j in numbers])
#     n_number = [ [i,i] if len(i) == m  else [i,i+i[-1]*(m-len(i))] for i in numbers]
#     n_number = sorted(n_number, key = lambda x:x[1], reverse = True)
#     answer = ''
#     for i in range(len(n_number)):
#         answer+=n_number[i][0]

#     return answer


# 통과한 풀이
def solution(numbers):
    numbers = list(map(str,numbers)) # 정수로 된 요소들을 문자형으로 변경
    numbers = [[i,i*3] for i in numbers] # 문자열을 3배, 왜 3배? -> 1000 이하의 조건이라서
    # 문자열의 크기 비교는 첫 번째 인덱스를 아스키코드로 바꾸어 비교, 만약 같다면 그 다음 인덱스를 가지고 비교하기 때문
    numbers = sorted(numbers, key = lambda x:x[1], reverse = True) # 3배한 문자? 숫자?를 기준으로 내림차준으로 정렬
    answer = ''
    for i in range(len(numbers)):
        answer += numbers[i][0] # 내림차순한 순서대로 문자열에 추가하여 정답 초기화
        
    if int(answer) == 0: # 만약 모든 문자열이 0이라면
        return '0' # 하나의 문자 0으로 반환
        
    return answer

numbers = [3,34,30,5,9] # 9534330
numbers = [1,10,100,1000] # 11010010000
numbers = [9,998] # 9998
numbers = [30,3021] #303021
numbers = [0,0,0,0] # 0000
numbers = [40, 404] # 40440
print(solution(numbers))


'''테스트를 위한 코딩'''
# n = list(map(str,numbers))
# # print(max([len(i) for i in n]))
# m = max([len(j) for j in n])
# n_number = []
# for i in n:
#     if len(i) == m:
#         n_number.append([i,i])
#     else:
#         a = i+i[-1]*(m-len(i))
#         n_number.append([i,a])
        
# print(n_number)
# n_number = sorted(n_number, key = lambda x:x[1], reverse = True)
# print(n_number)
# answer = ''
# for i in range(len(n_number)):
#     answer+=n_number[i][0]
    
# print(answer)