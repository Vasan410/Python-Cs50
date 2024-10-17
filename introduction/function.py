# def
'''def hello(to):
    print("hello,", to)
name = input("whts your name? ")
hello(name)

def hello(to="world"):
    print("hello,", to)
hello()
name = input("whts your name? ")
hello(name)'''

def main():
    x = int(input("wht is x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()