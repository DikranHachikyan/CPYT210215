
if __name__ == '__main__':
    actions = {
        '+': lambda a,b: a + b,
        '/': lambda a,b: a / b,
        'q': quit
    }

    while True:
        try:
            a = float(input('value of a:'))
            op = input('Action (+,-,*,/):')
            if op == 'q':
                actions['q']()
            b = float(input('value of b:'))

            print(f'{a} {op} {b} = {actions[op](a,b)}')
        except (ValueError, KeyError) as e:
            print(f'Unsupported operation or Not a number:({e})')
        except Exception as e:
            print(f'Unknown error ({e})')
        else:
            continue
        finally:
            print('--- finally ---')