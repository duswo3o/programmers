'''
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
'''


def solution(n):
    n_bin = bin(n)[2:] # n의 2진수 표현
    print(n_bin)
    cnt = n_bin.count('1') # 1의 개수
    r_bin = ''.join(list(reversed(list(n_bin))))
    
    # 전부 1일 경우
    if cnt == len(n_bin):
        answer = n_bin.replace('1','10',1)
        
    # 1과 0이 섞여있는 경우
    else:
        idx = r_bin.find('10') # '10'의 인덱스 저장
        answer = r_bin.replace('10','01',1) # 가장 먼저 있는 '10'을 '01'으로 바꾸기
        new = []
        if idx>=0: # '10'이 처음에 있지 않은 경우
            cnt = answer[:idx].count('1') # '01' 앞의 숫자들의 1의 개수를 반환하여
            if cnt>=0:
                for i in range(len(answer[:idx])): # 길이만큼 반복문 실행
                    if cnt>0: # '10' 앞의 1의 개수만큼 1을 추가
                        new.append('1')
                        cnt-=1
                    else:
                        new.append('0')
            # print(new)
            new = ''.join(new) # '10'이전의 숫자 완성하기
            answer = new+answer[idx:]  # '10'이후의 숫자와 이전의 숫자 합쳐서 문자열 반환
            answer = ''.join(list(reversed(list(answer)))) # 다시 뒤집어 원래대로 반환
            
        # 2진수에 '01'이 없는 경우
        elif idx == -1:
            new = list(n_bin[1:])
            new.reverse()
            new = ''.join(new)
            answer = '10'+new
        
        print(answer)         
    return int('0b'+answer,2) #2진수를 10진수로 변환

            
        
print(solution(60335700574206))
# print(bin(60335700574206)[2:])
# print(int('0b10001',2))
