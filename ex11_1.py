def main():
    num = float(input('num = '))
    output = ''

    if num >= 0:
        output = 'positive'
    else:
        output = 'negative'

    print(f'{num} is {output}')
    print('----')
    

#------------
main()