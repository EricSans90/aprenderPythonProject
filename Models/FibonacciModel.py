class FibonacciModel:
    a = 0
    b = 0
    c = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b

    def calculateNextValue(self):
        x = self.b + self.c
        self.a = self.b
        self.b = self.c
        self.c = x

    def printNextValue(self):
        return " a: "+ str(self.a) + " b: " + str(self.b) +  " c: " +  str(self.c)