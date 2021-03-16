# 1. дефиниция на класа
class Point:
    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('--- object ctr. ---')
        #данни на класа
        self.x = x
        self.y = y
    
    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point(10,20)
    p2 = Point()

    p1.draw()
    p2.draw()

    p1.move_to(40, -15)

    p1.draw()