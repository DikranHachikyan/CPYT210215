# 1. дефиниция


if __name__ == '__main__':
    # 2. извикване
    values = ( v + 2 for v in range(5, 31, 5))

    print(f'1 -> values = {next(values)}')
    print(f'2 -> values = {next(values)}')
    print(f'3 -> values = {next(values)}')
    print(f'4 -> values = {next(values)}')
    print(f'5 -> values = {next(values)}')

    arr = list(values)
    print(f'arr = {arr}')