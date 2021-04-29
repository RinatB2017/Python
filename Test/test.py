
class A(object):
    def print_A(self):
        print("A")

    def __priv(self):
        print("Private")

class B(A):
    def print_B(self):
        print("B")

class Test(object):
    def test(self):
        print("Test")

def read_file():
    with open('notebook.txt') as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    print("OK")
    test = Test();
    test.test()

    class_b = B();
    class_b.print_A()
    class_b.print_B()

    # f = open("notebook.txt", "r")
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    # f.close()

    read_file()
