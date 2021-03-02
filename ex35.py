# 1. дефиниция

def show(title, a = 100, *args, kw1 = 'A', kw2 = 'B', **kwargs):
    print(f'title:{title}')

    print(f'a = {a}')

    print('args:')
    for v in args:
        print(f'arg:{v}', end = ' ')
    print()

    print('kwargs:')

    kw_params = {
        'path': kwargs.get('path','./'),
        'log' : kwargs.get('log', './app.log')    
    }

    print(f'path = {kw_params["path"]}, log = {kw_params["log"]}')
    
    print('keyword-only args')
    print(f'kw1 = {kw1}, kw2 = {kw2}')


if __name__ == '__main__':
    # 2. извикване
    show('Text Editor')

    show('Text Editor', 12)

    show('Text Editor', 15, *(1, 2, 3, 4, 5))


    show('Text Editor', 15, *(1, 2), path = '/usr/local/', log = '/var/log/messages')

    show('Text Editor', 15, *(1, 2),  log = '/var/log/messages1',path = '/usr/local1/')

    app_conf = {
        'app':'Text Editor',
        'version':'1.2',
        'path': '/usr/local/te',
        'proc': 10
    }

    show('Text Editor', 15, 1, 2,  **app_conf)


    show('Text Editor', 15, 1, 2, kw1 = 'X',  **app_conf)

    show('Text Editor', kw1 = 'Y', kw2 = 'Z',  **app_conf)