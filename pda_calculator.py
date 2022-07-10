"""Calculator implementation using PDA for calculating the result of a mathematical expression."""
import re
import math


class Stack:
    """Class Stack for implementing a stack and its operations."""
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError('Stack is empty!')

        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return IndexError('Stack is empty!')

        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True

        return False


class Calculator:
    """Class Calculator for calculating a mathematical expression using PDA"""
    def __init__(self, infix: str):
        self.precedence = {'(': 0, 'sin': 0, 'cos': 0, 'ln': 0, 'sqrt': 0, 'abs': 0, '+': 1, '-': 1, '*': 2,
                        '/': 2, '^': 3}
        self.infix = infix
# fasele
    def separator(self):
        """
        Function separator for splitting the input letters.
        :return: a list
        """
        i = 0
        while i < len(self.infix):
            if self.infix[i] == '(' and i + 1 < len(self.infix):
                self.infix = self.infix[:i] + ' ' + self.infix[i] + ' ' + self.infix[i + 1:]
                i += 2
            elif self.infix[i] == ')' and i - 1 >= 0:
                self.infix = self.infix[:i] + ' ' + self.infix[i] + ' ' + self.infix[i + 1:]
                i += 3
            else:
                i += 1

        return self.infix.split()
    # be tartib oleviat
    def infix_to_postfix(self):
        """
        A function for converting an infix expression to a postfix expressing using a stack.

        :return: The postfix expression split to a list
        """
        stack = Stack()
        result = []
        separated_list = self.separator()
        for index in separated_list:
            if bool(re.match("^\\d+$", index)):
                result.append(int(index))
            elif bool(re.match("^\\d+\\.\\d+$", index[1:])):
                result.append(float(index))
            elif '(' in index:
                stack.push(index)
            elif index in ['sin', 'cos', 'tan', 'sqrt', 'abs', 'ln']:
                stack.push(index)
            elif index == ')':
                while not stack.is_empty() and stack.top() != '(':
                    result.append(stack.pop())

                try:
                    stack.pop()
                except IndexError:
                    print('INVALID')
                    quit()
            else:
                if index in ["+", "-", "*", "/"]:
                    while not stack.is_empty() and self.precedence[index] <= self.precedence[stack.top()]:
                        result.append(stack.pop())

                    stack.push(index)
                elif index == "^":
                    while not stack.is_empty() and self.precedence[index] < self.precedence[stack.top()]:
                        result.append(stack.pop())

                    stack.push(index)

        while not stack.is_empty():
            result.append(stack.pop())

        return result
    # javap push to stack 
    def evaluate(self):
        """
        Function evaluate for calculating the final answer from the postfix expression.

        :return: A str including the answer to the expression
        """

        stack = Stack()
        postfix = self.infix_to_postfix()
        for index in postfix:
            if isinstance(index, int) or isinstance(index, float):
                stack.push(index)
            elif 'sin' in index:
                stack.push(math.sin(stack.pop()))
            elif 'cos' in index:
                stack.push(math.cos(stack.pop()))
            elif 'tan' in index:
                stack.push(math.tan(stack.pop()))
            elif 'ln' in index:
                stack.push(math.log(stack.pop(), math.e))
            elif 'sqrt' in index:
                stack.push(math.sqrt(stack.pop()))
            elif 'abs' in index:
                stack.push(abs(stack.pop()))
            else:
                first = stack.pop()
                second = stack.pop()

                if index == "+":
                    stack.push(first + second)
                elif index == "-":
                    stack.push(second - first)
                elif index == "*":
                    stack.push(second * first)
                elif index == "/":
                    stack.push(round(second / first, 2))
                elif index == "^":
                    stack.push(second ** first)
                else:
                    raise Exception("Error")

        return '{0:.2f}'.format(stack.pop())



# input_line = input()
# expression = Calculator(input_line)
# print(expression.evaluate())
try : 
    input_line = input()
    expression = Calculator(input_line)
    # mmd = Calculator.separator(input_line)
    # print(mmd) 
    print(expression.evaluate())
except : 
    print("INVALID")