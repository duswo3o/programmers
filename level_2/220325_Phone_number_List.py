'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
'''

def solution(phone_book):
    # 리스트 정렬
    phone_book = sorted(phone_book, key = lambda x:(x,len(x))) # 값을 기준으로 먼저 정렬하고, 길이를 기준으로 한 번 더 정렬
    
    for i in range(len(phone_book)-1): # 반복문 실행
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # 다른 번호의 접두어가 된다면
            return False # false 반환
        
    return True # 접두어가 아니면 true 반환
    
        
        
    
phone_book = ["934793", "34", "44", "9347"] # false
# phone_book = ["123","456","789"] # true
# phone_book = ['12','123','13'] # false
print(solution(phone_book))