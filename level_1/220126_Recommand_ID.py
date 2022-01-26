'''
신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, 
"네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
def solution(new_id):
    
    # 1단계 : 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    id = ''
    # 2단계 : 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)이외의 문자 제거
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            id +=i
            
    # 3단계 : 마침표(.)가 연속일 때 한 개로 교체
    while ('..' in id):
        id = id.replace('..','.')
    
    # 4단계 : 마침표(.)가 처음과 끝에 위치할 때 제거하기
    if id=='.':
        id = 'a'
    if id[0]=='.' and len(id)!=0:
        id = id[1:]
    if id[-1]=='.' and len(id)!=0:
        id = id[:len(id)-1]
    
    # 5단계 : 빈 문자열이면 "a" 대입
    if id == '':
        id+='a'
    
    # 6단계 : 길이가 16이상이면 첫 15개까지, 15번째가 마침표(.)면 제거
    if len(id)>15:
        id = id[:15]
    if id[-1]=='.':
        id = id[:len(id)-1]
    
    # 7단계 : 길이가 2 이하이면 마지막 문자를 길이가 3이 될때까지 반복
    while(len(id)<3):
        id += id[-1]
    
    
    return id
            

# new_id = '...!@BaT#*..y.abcdefghijklm.'
# new_id = 'z-+.^.'
new_id = '=.='
# new_id = '123_.def'
# new_id = 'abcdefghijklmn.p'

print(solution(new_id))
