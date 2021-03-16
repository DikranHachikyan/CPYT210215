def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError:
        raise

if __name__ == '__main__':
    connection = {
        'host':'localhost',
        'port': 1521,
        'service': 'oracle'
    }

    try:
        find_key('service', **connection)
        find_key('ip', **connection)
    except KeyError as e:
        print(f'invalid key:({e})')