# 1. дефиниция

# глобална променлива
port = 8080

def sum_numbers(a, b, *args):
    # c - локална променлива (вижда се само тук)
    print(f'args:{args}')
    c = a + b

    for v in args:
        c += v

    return c



if __name__ == '__main__':
    # 2. извикване
    res1 = sum_numbers(5, 6)

    x, y, z = 10, 12, 20

    res2 = sum_numbers(x, y, z)

    res3 = sum_numbers(x, y, z, 1, 2, 3, 4, 5)

    t = [1, 2, 3, 4, 5]

    res4 = sum_numbers(x, y , z, *t)

    print(f'res1 = {res1} res2 = {res2} res3 = {res3} res4={res4}')
    