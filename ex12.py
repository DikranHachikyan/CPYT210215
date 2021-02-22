def new_file():
    return 'create a new file'

def open_file():
    return 'open file'

def save_file():
    return 'save file'

def quit_editor():
    print('Quit Editor')
    quit()

def main():
    # dict commands
    actions = {
        'n': new_file,
        'o': open_file,
        's': save_file,
        'q': quit_editor
    }
    
    ch = input('Command (n-new, o-open, s-save, q-quit):')

    if ch in actions:
        result = actions[ch]()
        print(f'action: {result}')
    else:
        print(f'Unknown command:{ch}')
        
    print('----')
    

#------------
main()