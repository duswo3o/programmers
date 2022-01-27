'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(n,lost,reserve):
    sports = {}
    for i in range(n):
        sports[i+1] = 1
    for i in lost:
        sports[i]=0
    for i in reserve:
        if i in lost:
            sports[i]=1
        else:
            sports[i]=2
            
    sports = dict(sorted(sports.items()))
    
    if sports[1]==0 and sports[2]==2:
        sports[1]+=1
        sports[2]-=1
    
    if sports[n]==0 and sports[n-1]==2:
        sports[n]+=1
        sports[n-1]-=1
    
    for i in range(n//2):
        if sports[i+1]==0 and i!=0:
            if sports[i]==2:
                sports[i+1]+=1
                sports[i]-=1
                pass
            elif sports[i+2]==2:
                sports[i+2]-=1
                sports[i+1]+=1
    
    for i in range(n,n//2,-1):
        if sports[i]==0 and i!=n:
            if sports[i+1]==2:
                sports[i]+=1
                sports[i+1]-=1
                pass
            elif sports[i-1]==2:
                sports[i]+=1
                sports[i-1]-=1
                
    if sports[n//2]==0 and n//2!=1:
        if sports[(n//2)+1]==2:
            sports[n//2]+=1
            sports[(n//2)+1]-=1
            pass
        elif sports[(n//2)-1]==2:
            sports[n//2]+=1
            sports[(n//2)-1]-=1
                
        
    count = 0            
    for i in list(sports.values()):
        if i>0:
            count+=1
           
    return count

n = 6
lost = [1,3,5]
reserve = [2,4,6]

print(solution(n, lost, reserve))
