'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 
홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
'''


def solution(s):
    answer = []
    for i in range(len(s.split(" "))):
        st = []
        for j in range(len(s.split(" ")[i])):
            if j%2==0:
                st.append(s.split(" ")[i][j].upper())
            else:
                st.append(s.split(" ")[i][j].lower())
        answer.append(''.join(st))
                
    return ' '.join(answer)


# s = "try hello world"



# print(s.split()[0][0])
# print(solution(s))

