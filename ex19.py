def main():
    # 2 + 4 + ... + 98 + 100 = 2550
    i = 0
    suma = 0

    while i <= 100:
        i += 1
        if i == 3: break
        suma += i
    else:
        print('--- else ---')

    print(f'1 + 2 + ... + 99 + 100 = {suma}')
    print('----')
    

#------------
main()