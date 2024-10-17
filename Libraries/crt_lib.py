def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")    
# using __name__ variable to overcome the bug:
if __name__ == "__main__":
    main()