def main():
    num = float(input('num = '))
    
    # (condition)? true_expr:false_expr

    m = 10 if num >= 0 else -1
    print(f'm = {m}')
    # if num >= 0:
    #     m = 10
    # else:
    #     m = -1

    print('----')
    

#------------
main()