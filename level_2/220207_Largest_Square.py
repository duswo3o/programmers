'''
1와 0로 채워진 표(board)가 있습니다. 
표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. 
(단, 정사각형이란 축에 평행한 정사각형을 말합니다.)
'''


def solution(board):
    
    # 하나의 행으로 이루어진 경우
    if type(board[0])==int: 
        if sum(board)!=0: # 모든 원소가 0이 아닌 경우
            return 1 # 1을 반환
        else: # 모든 원소가 0인 경우
            return 0 # 0을 반환
        
    # 하나의 열로 이루어진 경우
    elif type(board[0])==list and len(board[0])==1:
        if sum(sum(board,[])) != 0: # 모든 원소가 0이 아닌 경우
            return 1 # 1을 반환
        else: # 모든 원소가 0인 경우
            return 0 # 0을 반환
    
    # 두 개 이상의 행과 열로 이루어진 경우    
    else:
        l  = 0 # 최대 값을 저장할 변수 초기화 (최대값을 바로 업데이트 해 줘야 효율성을 통과함)
        for i in range(1,len(board)): # (1,1)에 있는 원소부터 시작해서
            for j in range(1,len(board[0])):
                if board[i][j]!=0: # 해당 원소가 0이 아닌 경우에
                    board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1]) # 왼쪽, 위, 왼쪽 위의 원소들 중 최솟값을 더함
                if board[i][j]>l: # 만약 위치의 원소가 현재 최대값보다 크다면
                    l = board[i][j] #최대값 업데이트
                
    return l**2 # 넓이 반환


board = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
print(solution(board))