'''
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 
명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 
좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.
명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
'''

def solution(dirs):
    x, y = 0, 0 # 현재 x좌표와 y좌표 저장
    route = set() # 경로를 저장할 집합 -> 같은 길을 가면 추가가 안 되도록 집합으로 경로 설정
    for i in dirs:
        # 현재 위치와 이동 위치의 좌표값을 하나의 원소로 묶어 집합에 저장
        # 집합에서 ((x,y),(x,y-1))과 ((x,y-1),(x,y))은 다른 요소로 취급하기 때문에 빼기는 앞의 좌표에 더하기는 뒤의 좌표에 함
        if i == 'U'and y<5:
            route.add(((x,y),(x,y+1))) 
            y+=1
        elif i == 'D' and y>-5:
            route.add(((x,y-1),(x,y)))
            y-=1
        elif i=='R' and x<5:
            route.add(((x,y),(x+1,y)))
            x+=1
        elif i=='L' and x>-5:
            route.add(((x-1,y),(x,y)))
            x-=1
            
    return len(route) # 집합의 개수 반환

dirs = "ULURRDLLU"
print(solution(dirs))