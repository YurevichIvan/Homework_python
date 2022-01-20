import sys


def add(argv):
    if not argv:
        return 1
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        for i in argv:
            s = i.replace(',', '')
            if s.isdigit() == True:
                file.write(i + '\n')

    return 0


if __name__ == '__main__':
    exit(add(sys.argv))

