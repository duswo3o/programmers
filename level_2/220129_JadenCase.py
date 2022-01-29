'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
'''

def solution(s):
    s = s.split(' ')
    answers = []
    for i in range(len(s)):
        answer = ''
        if s[i]=='':
            answer+='-'
        else:
            if s[i][0].isalpha():
                answer += s[i][0].upper()
            else:
                answer += s[i][0]
        answer += s[i][1:].lower()
        answers.append(answer)

    answers = ' '.join(answers)

    return answers.replace('-','')

s = "3people unFollowed  me"	
print(solution(s))
