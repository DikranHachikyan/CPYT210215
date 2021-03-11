
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
    except KeyError:
        print(f'Unsupported operation:{op}')
    except ValueError:
        print(f'Not a number')
    except:
        print('Unknown error')
    else:
        print('--- else ---')
    finally:
        print('--- finally ---')