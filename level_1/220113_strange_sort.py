'''
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
'''

def solution(strings,n):
    my = {}
    my_string = []
    for i in sorted(strings):
        my[i]=i[n]
    answer = list(dict.fromkeys(sorted(my.values())))
    for j in answer:
        for key, value in my.items():
            if value == j:
                # print(key)
                my_string.append(key)
    # [my[i] for i in sorted(my.keys())]
        
    return my_string

print(solution(["abce", "abcd", "cdx"],2))
print(solution(["sun", "bed", "car"],1))
# ["sun", "bed", "car"]
# print(sorted(["abce", "abcd", "cdx"]))