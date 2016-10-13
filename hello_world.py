import sys

def name():
    for arg in sys.argv[1:]:
        print("Hello " + arg + "!")

def world():
    print("Hello World!")

def hello_world():
    if len(sys.argv) > 1:
        name()
    else:
        world()

hello_world()


