import math

def solution(num):
    return (math.sqrt(num)+1)**2 if math.sqrt(num) == int(math.sqrt(num)) else -1
