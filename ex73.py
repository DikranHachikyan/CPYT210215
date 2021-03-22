

def suma(a: float, b:float)->float:
    return a + b

if __name__ == '__main__':

    print('4 + 7:', suma(4,7))
    
    print('Py + thon:', suma('Py', 'thon'))

    print(suma.__annotations__)