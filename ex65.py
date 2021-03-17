from math import sqrt

class A:
    pass

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



if __name__ == '__main__':
    # 2. създаване на обект от тип Point
    p1 = Point(5,6)
    p2 = Point(7,8)
    a = A()

    p = p1 + p2
    print(f'{p1} + {p2} = {p}')

    p =  p1 + 5.7
    print(f'{p1} + 5.7 = {p}')
    

    if p2 > p1:
        print(f'{p1} < {p2}')
    else:
        print(f'{p1} >= {p2}')