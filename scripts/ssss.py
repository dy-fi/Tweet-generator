import inspect

def printInspect(name):
    lines = inspect.getsource(name)
    print(lines)

if __name__ == '__main__':
    name = sys.argv[1]
    printInspect(name)

# source scripts analyzer
This is a simple script for getting the lower level of code inside of python,
for achieving O(1) lookup time for [arbitrary indexes in dictionaries](https://www.oreilly.com/library/view/high-performance-python/9781449361747/ch04.html)
Don't actually use the code they used in your stuff though

'''
import inspect
lines = inspect.getsource('')
print(lines)
'''
put anything inside the ''
