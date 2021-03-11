def by_idx1(el):
    return el[1]

if __name__ == '__main__':
    pw2 = lambda a: a ** 2
    foo = lambda a: a ** 2 if a % 2 else a ** 3

    # 1.
    # print(f'pw2(5) = {pw2(5)}') 
    # print(f'foo(2) = {foo(2)}')
    # print(f'foo(5) = {foo(5)}')

    items = [('A', 5, 7), ('D', 2, 6), ('B', 4, 8), ('D', 2, 5)]
    # 2.
    # items.sort()

    # 3.
    # items.sort(key = by_idx1 )
    # items.sort( key = lambda el: el[1])
    items.sort( key = lambda el: (el[1], el[0], el[2]) )
    print(f'sorted items:{items}')

    vals = [5,6,7,8]

    for v in map( lambda e: e ** 2, vals):
        print(v)