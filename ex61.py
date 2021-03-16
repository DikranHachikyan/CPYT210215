# 1. дефиниция на класа
class Point:
    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('--- object ctr. ---')
        #данни на класа
        self.__x = x
        self.__y = y
    
    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.__x}, {self.__y})')

    def move_to(self, dx = 0, dy = 0):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point()
    p2 = Point()

    # динамично добавен атрибут (само за обекта, не за класа)
    p1.x = 25
    print(f'p1.x = {p1.x}')
    
    print(f'p2.x = {p2.x}')
    # print(f'p1: ({p1.__x},{p1.__y})')
    # p1.move_to(19,1)
    # p1.draw()