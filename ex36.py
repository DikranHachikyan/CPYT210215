# 1. дефиниция
# 5 + 4 + 3 + 2 + 1 + 0 
def sum_numbers(n):
    print(f'n = {n}')

    if n > 1:
        return n + sum_numbers(n-1)
    return 1


if __name__ == '__main__':
    # 2. извикване
    n = 5
    result = sum_numbers(n)

    print(f'1+2+...+{n} = {result}')