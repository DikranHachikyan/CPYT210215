# 1. дефиниция

def foo(a = [], b = {}):
    print(f'a = {a}')
    print(f'b = {b}')
    print('-' * 30)
    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == '__main__':
    # 2. извикване
    foo()
    # foo([1,2,3], {'A':100})
    foo()
    # foo([11,22,33,56,77], {'A':100, 'B':11, 'C':1})
    foo()