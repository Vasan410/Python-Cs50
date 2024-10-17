def main():
    name = int(input("Wht is x? "))
    print(hello(name))

def hello(to = "world"):
    return f"hello, {to}"

if __name__ == "__main__" :
    main()