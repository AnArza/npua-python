from calculator import Calculator

calculator = Calculator()
expression = '3.5 + 4.5 * 2 - 10 / 2'
result = calculator.calculate(expression)
print(f'{expression} = {result}')