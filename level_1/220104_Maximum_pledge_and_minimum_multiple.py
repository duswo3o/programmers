'''
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, 
solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
'''


def solution(n,m):
    answer = []

    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i ==0:
            answer.append(i)
            break
    for i in range(max(m,n),m*n+1):
        if i%n==0 and i%m==0:
            answer.append(i)
            break
            
    return answer
