

class Number:
    def __getattr__(self, attr):
        ch = attr[0]
        n  = int(attr[1::])

        if ch == 'b':
            return bin(n)
        elif ch == 'o':
            return oct(n)
        elif ch == 'x':
            return hex(n)
        
        raise AttributeError('valid prefixes b|o|x')


if __name__ == '__main__':
    num = Number()

    print(num.x12) # Hex
    print(num.o8) # Oct
    print(num.b10 ) # Bin