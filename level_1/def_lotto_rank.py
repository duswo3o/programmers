def ranking(score):
    if score == 6:
        return 1
    elif score == 5:
        return 2
    elif score == 4:
        return 3
    elif score == 3:
        return 4
    elif score == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    
    result = []
    
    same = 0
    zero_count = 0
    for l in lottos:
        if l == 0:
            zero_count+=1
            

    for i in range(6):
        if lottos[i] != 0:
            for j in range(6):
                if lottos[i] == win_nums[j]:
                    same += 1
                    
    diff = 6 - same - zero_count
    
    result.append(ranking(6-diff))
    result.append(ranking(same))
    
    return result