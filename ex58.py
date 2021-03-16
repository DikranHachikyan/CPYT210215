# 1. дефиниция на класа
class Point:
    # Конструктор на класа
    def __init__(self):
        #данни на класа
        self.x = 10
        self.y = 20


if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point()
    p2 = Point()

    print(f'p1:({p1.x}, {p1.y})')

    p1.x = 1
    print(f'p1:({p1.x}, {p1.y})')
    print(f'p2:({p2.x}, {p2.y})')
