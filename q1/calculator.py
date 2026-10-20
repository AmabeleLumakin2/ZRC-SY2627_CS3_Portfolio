class ArithmeticOperations:

    def __init__(self, firstValue, secondValue):
        self.firstValue = firstValue
        self.secondValue = secondValue

    def addition(self):
        result = self.firstValue + self.secondValue
        print(f"The sum of numbers {self.firstValue} and {self.secondValue} is {result}")

    def subtraction(self):
        result = self.firstValue - self.secondValue
        print(f"The difference of numbers {self.firstValue} and {self.secondValue} is {result}")

    def multiplication(self):
        result = self.firstValue * self.secondValue
        print(f"The product of numbers {self.firstValue} and {self.secondValue} is {result}")

    def division(self):
        result = self.firstValue / self.secondValue
        print(f"The quotient of numbers {self.firstValue} and {self.secondValue} is {result}")

firstValue = input("Enter a Number: ")
secondValue = input("Enter a second Number: ")

AO = ArithmeticOperations(int(firstValue), int(secondValue))

AO.addition()
AO.subtraction()
AO.multiplication()
AO.division()

