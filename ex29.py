# 1. дефиниция

# глобална променлива
port = 8080

def sum_numbers(a, b):
    # c - локална променлива (вижда се само тук)
    c = a + b
    return c



if __name__ == '__main__':
    # 2. извикване
    res1 = sum_numbers(5, 6)

    x, y = 10, 12

    res2 = sum_numbers(x, y)

    print(f'res1 = {res1} res2 = {res2}')
    