
from draw.point import Point
from draw.rectangle import Rectangle
from math import sqrt

class ShapeUtils:
    p0 = Point()

    @staticmethod
    def distance(p1,p2):
        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError('Params must be points')
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return sqrt( dx ** 2 + dy ** 2)

    @staticmethod
    def compare(p1,p2):
        '''
            Return:
            neg. value p1 < p2
            zero       p1 == p2
            pos. value p1 > p2
        '''
        dist1 = ShapeUtils.distance(p1, ShapeUtils.p0)
        dist2 = ShapeUtils.distance(p2, ShapeUtils.p0)

        return dist1 - dist2


if __name__ == '__main__':
    p1 = Point(9,8)
    p2 = Point(6,4)

    print(f'dist btw {p1} and {p2} is : {ShapeUtils.distance(p1,p2)}')

    if ShapeUtils.compare(p1,p2) > 0:
        print(f'{p1} > {p2}') 