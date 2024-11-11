class A:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def print_val(self):
        print(self.name, self.age)

s = A('abc', 50)
s.print_val()