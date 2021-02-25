def main():
    users = ['anna', 'maria','markus','john', 'florian']
    mails = ['anna@no.com', 'maria@no.com','markus@no.com','john@no.com']

    for data in zip(users, mails):
        user, mail = data 
        print(f'value: {user} => {mail}')
        
    print('----')
    

#------------
main()