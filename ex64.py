# 1. дефиниция на класа
class Point:
    # променлива на класа (статична)
    label = 'A'
    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('--- object ctr. ---')
        # данни на обекта
        self.__x = x
        self.__y = y
        Point.label = 'S'
    
    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.__x}, {self.__y})')

    def move_to(self, dx = 0, dy = 0):
        self.__x += dx
        self.__y += dy
    
    # Специални методи
    # function override
    def __str__(self):
        '''Object as String'''
        return f'({self.__x},{self.__y})'
        # return 'object point'

if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point(5,6)

    print(f'point p1:{p1}')

    txt = str(p1)
    print(p1)