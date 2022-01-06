def solution(n):
    num = []
    for i in range(len(str(n))):
        num.append(str(n)[i])
        
    num.sort(reverse=True)
    
    s=''
    for j in range(len(num)):
        s=s+num[j]
        
    return int(s)
    