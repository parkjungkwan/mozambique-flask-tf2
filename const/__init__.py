if __name__ == '__main__':
    def calc():
        a = 3
        b = 5
        c = 0
        def la(x):
            nonlocal c
            c = a * x + b
            print("클로저: "+str(c))
        return la
    c = calc()
    c(1)