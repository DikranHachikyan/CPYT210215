# 1. дефиниция

c = 8080

def show():
    global c
    c = 1
    print(f'c = {c}')
    # x = c
    # print(f'x = {x}')

if __name__ == '__main__':
    # 2. извикване
    print(f'before c = {c}')
    show()
    print(f'after c = {c}')