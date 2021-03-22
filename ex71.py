
from draw.point import Point
from draw.rectangle import Rectangle

if __name__ == '__main__':
    rc = Rectangle(100, 200, 500, 800)

    print(f'Rectangle : {rc}')

    rc.draw()

    rc1 = Rectangle(5,7, 470,800)

    if rc > rc1:
        print(f'{rc} > {rc1}')
    else:
        print(f'{rc} <= {rc1}')

    print(f'Rectangle Area:{rc.area()}')