def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError:
        pass
        # print(f'invalid key:{key}')

if __name__ == '__main__':
    connection = {
        'host':'localhost',
        'port': 1521,
        'service': 'oracle'
    }

    find_key('service', **connection)
    find_key('ip', **connection)