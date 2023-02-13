class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multi(self):
        self.output = self.a * self.b
        return self.output


a = Calculator(10, 20)
print(a.multi())
