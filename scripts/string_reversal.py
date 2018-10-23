import sys

def reverse():
    for i in sys.argv[1:]:
        i = i[::-1]
        print(i)
reverse()
