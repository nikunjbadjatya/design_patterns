''' expression_parser.py

Program to verify whether the given INPUT_EXPRESSION is True or False.

How to Execute:
Modify INPUT_EXPRESSION and INPUT_JSON as per your needs below.
#python expression_parser.py

Algorithm:
1. Read the INPUT_JSON and make corrsponding python objects such that dot resolution works.
2. Evaluate the INPUT_EXPRESSION over the INPUT_JSON.

Assumptions:
1. INPUT_JSON is a valid json.
2. INPUT_EXPRESSION follows the standard:
   GT has only two operands
   BETWEEN has a list of two items
   IN is a list

Requirements:
Python2.7 or greater
Tested on Python2.7

Limitations:
1. Have used Python's eval method


Author:
Nikunj Badjatya
https://in.linkedin.com/in/celebratetech


'''

from operator_factory import OperatorFactory
from operator import OperationError

INPUT_JSON = {"user": {"address": {
                                    "address_line": "XYZ Street",
                                    "city": "San Francisco",
                                    "state": "",
                                    "zipcode": 94150
                                    },
                        "age": 30
                        }
            }

INPUT_EXPRESSION = ["AND",["EQ", "user.address.city", "San Francisco"], ["LT", "user.age", 34]]
#INPUT_EXPRESSION = ["OR",["EQ", "user.address.city", "San Francisco"], ["GT", "user.age", 34], ["EQ", "user.address.zipcode", 94150], ["BETWEEN", "user.address.zipcode", [94150, 94155]]]
#INPUT_EXPRESSION = ["BETWEEN", "user.address.zipcode", [94149, 94155]]

class JsonToObject(object):
    """
    Class which creates python objects based on the input json.
    It does that in a manner such that dot resolution works.
    """

    def __init__(self, d):
        for a, b in d.items():
            setattr(self, a, JsonToObject(b) if isinstance(b, dict) else b)

    def do_math(self, operator_as_str, *operands):
        """
        Method which performs the math over the operands
        """
        operator = OperatorFactory.get_operator(operator_as_str)

        try:
            return operator.do_operation(operands)
        except Exception, e:
            raise OperationError(e)


    def evaluate_json(self, expression):
        """
        Method to evaluate the expression on input json.
        It assumes that the expression will follow format [OPEARTOR, OPERAND, COMPARISON_VALUE]

        Here we identify the operator and the operands and call do_math() with those.
        """

        operand = []
        for i, item in enumerate(expression):
            operator_as_str = expression[0]
            # If the expression item is a list, then recurse.
            # Dont do this if first item is "IN" or "BETWEEN"
            if isinstance(item, list) and (operator_as_str not in ["IN", "BETWEEN"]):
                #
                if i >= 1:
                    operand.append(self.evaluate_json(item))
            elif i == 0:
                operator_as_str = item
            elif i == 1:
                exp = 'self.'+ item
                try:
                    operand.append(eval(exp)) # This returns the value after the dot resolution
                except Exception:
                    print "Input operand is not resolvable '%s'" % exp
            elif i == 2:
                operand.append(item)
        return self.do_math(operator_as_str, *operand)

def main():
    """
    Driver program for expression_parser.py
    """
    # Step-1
    # Create Python objects in desired format
    x = JsonToObject(INPUT_JSON)

    # Step-2
    # Evaluate the INPUT_EXPRESSION over the INPUT_JSON
    print x.evaluate_json(INPUT_EXPRESSION)

if __name__ == '__main__':
    main()
