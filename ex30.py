# 1. дефиниция

# глобална променлива
port = 8080

def sum_numbers(a, b, d = 0):
    # c - локална променлива (вижда се само тук)
    c = a + b + d
    return c



if __name__ == '__main__':
    # 2. извикване
    res1 = sum_numbers(5, 6)

    x, y, z = 10, 12, 20

    res2 = sum_numbers(x, y, z)

    print(f'res1 = {res1} res2 = {res2}')
    