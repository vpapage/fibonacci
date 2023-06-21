import os

ARCH = os.environ.get('ARCH', 'Undefined')

def main():
    print("Hello, my architecture is", ARCH)

if __name__ == "__main__":
    main()