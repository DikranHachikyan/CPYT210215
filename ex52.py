
if __name__ == '__main__':
    actions = {
        '+': lambda a,b: a + b,
        '/': lambda a,b: a / b
    }

    try:
        a = float(input('value of a:'))
        op = input('Action (+,-,*,/):')
        b = float(input('value of b:'))

        print(f'{a} {op} {b} = {actions[op](a,b)}')
    except KeyError as e:
        print(f'Unsupported operation:{op} ({e})')
    except ValueError as e:
        print(f'Not a number ({e})')
    except Exception as e:
        print(f'Unknown error ({e})')
    else:
        print('--- else ---')
    finally:
        print('--- finally ---')