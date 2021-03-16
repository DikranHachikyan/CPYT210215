# 1. дефиниция на класа
class Point:
    # Конструктор на класа
    def __init__(self):
        #данни на класа
        self.x = 10
        self.y = 20

    def draw(self):
        print(f'draw point at:({self.x}, {self.y})')


if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point()
    p2 = Point()

    p1.draw()

    p1.x = 11
    p1.y = 12

    p1.draw()
    p2.draw()