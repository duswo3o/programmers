'''
네오와 프로도가 숫자놀이를 하고 있습니다. 
네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(s):
    if "zero" in s:
        s = s.replace("zero","0")
    if "one" in s:
        s = s.replace("one","1")
    if "two" in s:
        s = s.replace("two","2")
    if "three" in s:
        s = s.replace("three","3")
    if "four" in s:
        s = s.replace("four","4")
    if "five" in s:
        s = s.replace("five","5")
    if "six" in s:
        s = s.replace("six","6")
    if "seven" in s:
        s = s.replace("seven","7")
    if "eight" in s:
        s = s.replace("eight","8")
    if "nine" in s:
        s = s.replace("nine","9")
        
    return int(s)
    
s = "1zerotwozero3"
print(solution(s))