def main():
    app_conf = {
        'title':'Text Editor',
        'version':'1.2',
        'path': '/usr/local/te',
        'proc': 10
    }

    for item in app_conf.items():
        key, value = item 
        print(f'key: {key} => {value}')
        
    print('----')
    

#------------
main()