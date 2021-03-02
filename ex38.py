# 1. дефиниция

def sort_priority(values, group):
    found = False
    def helper(el):
        nonlocal found
        if el in group:
            found = True
            return (0,el)
        return (1,el)

    values.sort(key = helper)
    return found

if __name__ == '__main__':
    # 2. извикване
    numbers = [1, 4, 5, 2, 3, 8, 9, 7, 6]
    group = {5, 4, 3}

    result = sort_priority(numbers, group)

    print(f'result = {result} numbers = {numbers}')