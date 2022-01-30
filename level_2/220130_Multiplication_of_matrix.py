'''
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
'''


def solution(arr1,arr2):
    answer = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            arr.append(sum([arr1[i][k]*arr2[k][j] for k in range(len(arr2))]))
        answer.append(arr)
        
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]	
arr2 = [[3, 3], [3, 3]]

print(solution(arr1,arr2))