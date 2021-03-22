# 1. 
# import draw.point as drw

# 2.
from draw.point import Point

# 3.
# from draw.point import Point as P
# p = P(1,2)

if __name__ == '__main__':
    # 1.
    # p1 = drw.Point(5,6)
    
    p1 = Point(5,6)

    p1.x = 12
    p1.y = 16

    print(f'p1: {p1} (n inst {Point.count})')
    
    p2 = Point(7,8)
    print(f'p2: {p2} (n inst {Point.count})')

    print(f'p1: {p1} (n inst {Point.count})')
    print(f'p2: {p2} (n inst {Point.count})')