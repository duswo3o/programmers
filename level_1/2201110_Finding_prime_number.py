
'''1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''
# def solution1(n):
#     li = []
#     for i in range(2,n+1,2):
#         if (len([j for j in range(1,i+1) if i%j==0])==2):
#             li.append(i)
#     return li


# import math
# def solution2(n):
#     li = [2]
#     for i in range(3,n+1,2):
#         a = len([j for j in range(1,int(math.sqrt(n))+1) if i%j==0 and i//j>1])
#         if a==1:
#             li.append(i)
    
#     return li


# def solution3(n):
#     if n>5:
#         li = [2,3]
#         for i in range(5,n+1,2):
#             if (len([j for j in range(1,i+1) if i%j==0])==2):
#                 li.append(i)
#         return li
#     else:
#         li_ = []
#         for i in range(2,n+1):
#             if (len([j for j in range(1,i+1) if i%j==0])==2):
#                 li_.append(i)
#         return li_


# def solution4(n):
#     li = [2]
#     for i in range(3,n+1,2):
#         a = len([j for j in range(1,int(n**0.5)+1) if i%j==0 and i//j>1])
#         if a==1:
#             li.append(i)
    
#     return len(li)
                
# def solution5(n):
#     s =[2]+ [i for i in range(3,n+1,2)]
#     # for a in s:
#     #     if (a!=2) and (a%2==0):
#     #         s.remove(a)
              
#     w = []
#     while len(s)!=0:
#         w.append(s[0])
#         for i in range(len(s)):
#             if i%s[0]==0:
#                 print("true: ",s[0],i, i%s[0])
#                 s.remove(s[0])
#                 # print(s)
#             else:
#                 print("false: ",s[0],i, i%s[0])
#     return w

        

# n=10
# li = []
# for i in range(2,n+1):
#     if (len([j for j in range(1,1+i) if i%j==0])==2):
#         li.append(i)
            
# print(li)
# print(len(li))
# print(s(5))
# print(int(math.sqrt(5)+1))

# print(solution(10))

# print([2,3]+[i for i in range(5,11,2)])

# s = [2,3,5,7,9,11,13,15,17,19,21]
# w=[]
# while len(s)!=0:
#     w.append(s[0])
#     s = [i for i in s if i%s[0]!=0]
    
# print(w)


# def solution6(n):
#     s =[2]+ [i for i in range(3,n+1,2)]
#     w = []
#     while len(s)!=0:
#         w.append(s[0])
#         s = [i for i in s if i%s[0]!=0]
    
#     return len(w)

def solution(n):
    s =[2]+ [i for i in range(3,n+1,2)]
    w = []
    while s[0]<n**0.5:
        w.append(s[0])
        s = [i for i in s if i%s[0]!=0]
    
    return len(w)+len(s)
