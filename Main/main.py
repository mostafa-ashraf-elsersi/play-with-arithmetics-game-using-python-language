# PlayWithArithmetics code

import random as rdm


class GeneratingEquations:
    def __init__(self):
        self.__first_operand = 0
        self.__second_operand = 0
        self.__third_operand = 0
        self.__fourth_operand = 0
        self.__first_operator = ''
        self.__second_operator = ''
        self.__third_operator = ''

    def operands(self):
        self.__first_operand = rdm.randint(1, 5)
        self.__second_operand = rdm.randint(6, 10)
        self.__third_operand = rdm.randint(11, 15)
        self.__fourth_operand = rdm.randint(16, 20)

    def operators(self):
        operators_list = ['*', '-', '+']
        self.__first_operator = operators_list[rdm.randint(0, 2)]
        self.__second_operator = operators_list[rdm.randint(0, 2)]
        self.__third_operator = operators_list[rdm.randint(0, 2)]

    @staticmethod
    def equation_assembly(self):
        self.operands()
        self.operators()
        generated_equation = f"{self.__first_operand} {self.__first_operator} {self.__second_operand} {self.__second_operator} " \
                             f"{self.__third_operand} {self.__third_operator} {self.__fourth_operand}"
        result = eval(generated_equation)
        return generated_equation, result
