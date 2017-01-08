''' operator.py

Python module which holds custom defined exception classes and operator classes.
Any operator in future must be added here.

do_operation() method must be defined for each operator added.

Requirements:
Python2.7 or greater
Tested on Python2.7

Author:
Nikunj Badjatya
https://in.linkedin.com/in/celebratetech

'''

class OperationError(Exception):
    """ Custom exception class for any error in operation performing"""
    pass

class Operator(object):
    """Base class for all the operators """
    def do_operation(self, operands):
        raise NotImplementedError("Not implemented error")

class AND(Operator):
    """Operator class which will return true if all elements of the list are true """
    def do_operation(self, operands):
        return all(operands)

class OR(Operator):
    """Operator class which will return true if any one element of the list is true """
    def do_operation(self, operands):
        return any(operands)

class NOT(Operator):
    """Operator class which does not need another operand (Unary operator) """
    def do_operation(self, operands):
        return not operands[0]

class BETWEEN(Operator):
    """Operands is of type [2, [1,3]] i.e. 2 is between 1 and 3"""
    def do_operation(self, operands):
        return operands[1][0] <= operands[0] <= operands[1][1]

class EQ(Operator):
    """Operator class which will return true if all elements of the list are equal"""
    def do_operation(self, operands):
        return len(set(operands)) <= 1

class GT(Operator):
    """Operator class which will return true if first operand is greater than second operand"""
    def do_operation(self, operands):
        return operands[0] > operands[1]

class LT(Operator):
    """Operator class which will return true if first operand is less than second operand"""
    def do_operation(self, operands):
        return operands[0] < operands[1]

class IN(Operator):
    """Operator class which will return true if first operand is part of second operand"""
    def do_operation(self, operands):
        return operands[0] in operands[1]
