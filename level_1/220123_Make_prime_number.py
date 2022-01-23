'''
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
'''

from itertools import combinations
def solution(nums):
    
    Choose_three = list(combinations(nums,3))
    
    hap = []
    for i in range(len(Choose_three)):
        hap.append(sum(Choose_three[i]))
    
    answer = []
    for i in range(len(hap)):
        prime = 0
        for j in range(2,int(hap[i]**0.5+1)):
            if hap[i]%j==0:
                prime+=1
        if prime == 0:
            answer.append(hap[i])
        
    return len(answer)

nums = [1,2,3,4]
nums1 = [1,2,7,6,4]
print(solution(nums1))
