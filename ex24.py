def main():
    app_conf = {
        'title':'Text Editor',
        'version':'1.2',
        'path': '/usr/local/te',
        'proc': 10
    }

    for key in app_conf: 
        print(f'key: {key} => {app_conf[key]}')
        
    print('----')
    

#------------
main()