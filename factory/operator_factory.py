''' operator_factory.py

Python module which holds a factory class to return appropriate operator class.

Requirements:
Python2.7 or greater
Tested on Python2.7

Author:
Nikunj Badjatya
https://in.linkedin.com/in/celebratetech

'''

from operator import AND, OR, NOT, BETWEEN, GT, LT, EQ, IN

class OperatorFactory(object):
    """Factory class to return appropriate operator class"""

    @classmethod
    def get_operator(cls, operator_as_str):
        """Method to return appropriate operator class"""
        if operator_as_str.upper() == 'AND':
            return AND()
        elif operator_as_str.upper() == 'OR':
            return OR()
        elif operator_as_str.upper() == 'NOT':
            return NOT()
        elif operator_as_str.upper() == 'EQ':
            return EQ()
        elif operator_as_str.upper() == 'GT':
            return GT()
        elif operator_as_str.upper() == 'LT':
            return LT()
        elif operator_as_str.upper() == 'BETWEEN':
            return BETWEEN()
        elif operator_as_str.upper() == 'IN':
            return IN()
        else:
            raise Exception("Not a valid operator %s" % operator_as_str)
        # Similarly more classes can be added
