import sys

def show(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


if __name__ == '__main__':
    exit(show(sys.argv))

