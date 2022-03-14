'''
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 
길이 5 이하의 모든 단어가 수록되어 있습니다. 
사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 
이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
'''

def solution(word):
    vowel = ['A','E','I','O','U'] # 모음 사전
    order = 0 # 순서를 저장할 변수
    
    for i in range(len(word)): # 단어의 길이만큼 반복
        # 모음 사전의 순서대로 진행할 때
        if i == 0: # 첫 번째 문자가 바뀌면 781이 증가
            order+=781*vowel.index(word[i])+1
        elif i == 1: # 두 번째 문자가 바뀌면 156증가
            order+=156*vowel.index(word[i])+1
        elif i == 2: # 세 번째 문자가 바뀌면 31증가
            order+=31*vowel.index(word[i])+1
        elif i == 3: # 네 번째 문자가 바뀌면 6증가
            order+=6*vowel.index(word[i])+1
        elif i == 4: # 다섯번째 문자가 바뀌면 1증가
            order+=1*vowel.index(word[i])+1
    
    return order

word = "EIO"
print(solution(word))