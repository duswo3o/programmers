'''
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
'''

def solution(s):
    num = ['1','2','3','4','5','6','7','8','9','0']
    TF = [True if i in num else False for i in s]
    t = 0
    for i in TF:
        if i==True:
            t+=1
    
    return True if (len(s)==4 or len(s)==6) and t==len(s) else False
