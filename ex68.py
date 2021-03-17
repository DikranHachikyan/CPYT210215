from math import sqrt

class A:
    pass

# 1. дефиниция на класа
class Point:
    # променлива на класа (статична)
    label = 'A'
    count = 0

    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('--- object ctr. ---')
        # данни на обекта
        self.__x = x
        self.__y = y
        Point.label = 'S'
        Point.count += 1
    
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

    def __add__(self,other):
        # self - данни на левия операнд
        # other - данни на десния операнд
        # assert isinstance(other, Point), 'Right operand must be of type Point'
        
        if isinstance(other, Point):
            new_x = self.__x + other.__x
            new_y = self.__y + other.__y
        elif isinstance(other, (int, float)):
            new_x = self.__x + other
            new_y = self.__y + other
        else:
            # return NotImplemented
            raise NotImplementedError('Not implemented operation') 
        
        return Point(new_x, new_y) 

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError(f'Not implemented operation')

        dx1 = self.__x ** 2
        dy1 = self.__y ** 2
        dist1 = sqrt(dx1 + dy1)
        
        dx2 = other.__x ** 2
        dy2 = other.__y ** 2
        dist2 = sqrt(dx2 + dy2)

        return dist1 > dist2

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        assert x >= 0, 'x must be positive or zero'
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert y >= 0, 'y must be positive or zero'
        self.__y = y

    def __del__(self):
        '''Object Destr.'''
        Point.count -= 1


def show():
    # p3 - локална променлива
    p3 = Point(1,1)
    print(f'show p3: {p3} (n inst {Point.count})')



if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point(5,6)

    p1.x = 12
    p1.y = 16

    print(f'p1: {p1} (n inst {Point.count})')
    
    p2 = Point(7,8)
    print(f'p2: {p2} (n inst {Point.count})')

    show()
    print(f'p1: {p1} (n inst {Point.count})')
    print(f'p2: {p2} (n inst {Point.count})')