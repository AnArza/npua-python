from enum import Enum


class Operation(Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'


class Calculator:
    """
    A simple calculator that performs basic arithmetic operations
    (addition, subtraction, multiplication, division) on a given expression.

    Note:
    - The calculator processes the expression considering operator precedence.
    - The expression can contain numbers (including decimals), operators,
      and a period (`.`) for decimal points.
    - The calculator may not work correctly with invalid expressions.
    """

    def calculate(self, expression):
        expression = expression.replace(' ', '')
        elements = self._split_into_elements(expression)
        return self._evaluate(elements)

    def _split_into_elements(self, expression):
        elements = []
        num = ''
        operators = [op.value for op in Operation]

        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    elements.append(float(num))
                    num = ''
                if char in operators:
                    elements.append(char)
        if num:
            elements.append(float(num))

        return elements

    def _evaluate(self, elements):
        # handling the multiplication and the division firstly
        i = 0
        while i < len(elements):
            if elements[i] == Operation.MULTIPLY.value or elements[i] == Operation.DIVIDE.value:
                if elements[i] == Operation.MULTIPLY.value:
                    result = elements[i - 1] * elements[i + 1]
                else:
                    if elements[i + 1] == 0:
                        raise ZeroDivisionError
                    result = elements[i - 1] / elements[i + 1]
                elements[i - 1:i + 2] = [result]
                i -= 1
            else:
                i += 1
        # now handling the addition and the subtraction
        result = elements[0]
        for i in range(1, len(elements), 2):
            if elements[i] == Operation.ADD.value:
                result += elements[i + 1]
            elif elements[i] == Operation.SUBTRACT.value:
                result -= elements[i + 1]

        return result

