'''
2016년 1월 1일은 금요일입니다. 
2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다. 
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
'''

def solution(a,b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = 0
    for i in range(a):
        if i == 2:
            day += 29
        elif i==4 or i==6 or i==9 or i==11:
            day+=30
        elif i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            day+=31
            
    day+=b
    return week[day%7-1]

print(solution(5,24))