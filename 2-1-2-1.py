Y, M, D = map(int, input().split())

def yoon(Y):
    if Y % 4 == 0:
        return True
    elif Y % 4 == 0 and Y % 100 == 0:
        return False
    elif Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
        return True
    else:
        return False
    
def month(M):
    if M in (3,4,5):
        return 0
    elif M in (6,7,8):
        return 1
    elif M in (9,10,11):
        return 2
    else:
        return 3

def day(Y, M):
    if M in (1,3,5,7,8,10,12):
        return 31
    elif M in (4,6,8,11):
        return 30
    elif M == 2 and yoon(Y):
        return 29
    else:
        return 28

def season(Y, M, D):
    if month(M) == 0 and D <= day(Y, M):
        return "Spring"
    elif month(M) == 1 and D <= day(Y,M):
        return "Summer"
    elif month(M) == 2 and D <= day(Y,M):
        return "Fall"
    elif month(M) == 3 and D <= day(Y,M):
        return "Winter"
    else:
        return -1
    
print(season(Y,M,D))