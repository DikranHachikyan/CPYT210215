# 1. дефиниция на класа
class Point:
    # променлива на класа (статична)
    label = 'A'
    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('--- object ctr. ---')
        #данни на класа
        self.__x = x
        self.__y = y
        Point.label = 'S'
    
    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.__x}, {self.__y})')

    def move_to(self, dx = 0, dy = 0):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point(1,2)
    p2 = Point(4,6)

    print(f'label p1: {p1.label}')
    print(f'label p2: {p2.label}')
    Point.label = 'Z'
    print(f'label p1: {p1.label}')
    print(f'label p2: {p2.label}')
    # грешно
    # p1.label = 'X'
    print(f'label p1: {p1.label}')
    print(f'label p2: {p2.label}')