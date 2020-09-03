#!/usr/bin/python3
import hidden_4


def main():
    pass
if __name__ == "__main__":
    for i in dir(hidden_4):
        if i[0] != '_':
            print('{}'.format(i))
    main()
