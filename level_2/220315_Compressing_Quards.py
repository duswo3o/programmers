'''
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 
당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 
구체적인 방식은 다음과 같습니다.

당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 
각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 
배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
'''


def solution(arr):
    n = len(arr) # 배열의 길이
    comp = [0,0] # 0과 1의 개수를 반환할 리스트
    
    # 압축 함수
    def compression(a,b,n): # 압축할 행과 열, 길이
        st = arr[a][b] # 제일 처음 원소를 기준으로 같은지 아닌지 확인하기
        for i in range(a,a+n):
            for j in range(b,b+n):
                if arr[i][j]!=st: # 만약 가장 처음 값과 같지 않다면
                    nn=n//2 # 다시 분할하여 진행
                    # 재귀함수 형태로 호출
                    compression(a,b,nn)
                    compression(a+nn,b,nn)
                    compression(a,b+nn,nn)
                    compression(a+nn,b+nn,nn)
                    return
        comp[st]+=1 # 모든 값이 같다면 1 추가
    compression(0,0,n)
    return comp    
    
arr = [[1,1,0,0],
       [1,0,0,0],
       [1,0,0,1],
       [1,1,1,1]]

print(solution(arr))