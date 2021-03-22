from draw.point import Point
from draw.shape import Shape

class Rectangle(Point,Shape):

    def __init__(self, x = 0, y = 0, width = 0, height = 0, *args, **kwargs):
        super().__init__(x, y) # конструктор на родителя
        print('--- Rect Ctor. ---')
        # собствени данни
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        assert width >= 0, 'width must be >= 0'
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        assert height >= 0, 'height must be >= 0'
        self.__height = height

    # Специални методи

    def __str__(self):
        point_str = super().__str__()
        return f'{point_str}[{self.width}x{self.height}]'

    # function override
    def draw(self):
        # raise NotImplementedError('draw not implemented')
        super().draw()
        print(f'draw rectangle: {self}')

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        
        p = super().__gt__(other)
        return p and self.width * self.height > other.width * other.height