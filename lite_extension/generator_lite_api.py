"""


Name: Equation Generator
Version: 1.0.0 (stable)
Author: Frederik Munk Zino
Github: Velocity-plus (https://github.com/Velocity-plus)

--------------------------------------------------------------------------------------------------------------
Documentation:

- Idea
   This document contains code to supposedly generate mathematical reducible equations.
   It is not guaranteed that all equations generated are reducible, since they are randomly generated.
   This flaw can be solved by setting the correct parameter in 'FUNCTION <generate>' from 'CLASS ReducibleEQGen'

- Generating equations
  To generate random equations there are a lot of variables and decision factors that plays a role
  in the generation of the equations.

  The equation generator can be manipulated, so the generation is not only determined by randomness.
  You can change the following parameters, which are listed below:

  Parameters of function generate and multi_generate:
        :type int     :param n_gen: n
        :type tuple   :param difficulty: (min n, max n)
        :type tuple   :param exponent: min n, max n)
        :type tuple   :param numbers: (min n, max n)
        :type tuple   :param parentheses: (min n, max n)
        :type tuple   :param parentheses_exponent: (min n, max n)
        :type int     :param exponent_chance: = n
        :type tuple   :param char_amount: = (min n, max n)
        :type tuple   :param char_allowed: = ('a','b'.....)
        :type tuple   :param division_operators: = (min n, max n)
        :type boolean :param unique: boolean
        :type boolean :param reducible: boolean

  The listed variables that takes (min, n, max n) should be understood as the minimum possible number 
  the computer can generate and max n as the maximum number that can be generated (determined by randomization).
  fx: 
    => result = (1, 6)
    => Possible outputs: 1, 2, 3, 4, 5, 6 

  Defintion of variable:
    n_gen: How many equations should be generated (must be < 1000) 
    difficulty: how long the equation is fx (a+b) vs (a+b+c+d)...
    exponent:the exponents of the links in the equation fx (a^2+a^3)
    numbers: the numbers that can be generated in the equation fx (23a+54-2) (min and max)
    parentheses: how many parentheses that can be generated 

    parentheses_exponent: the exponent generated for the parentheses. If min n <= 1 and max n > 1, there is the
        possibility that some of the parentheses has no exponent or all of them

    exponent_chance: the chance of an exponent occurring at a parenthesis 
    char_amount: determines how many different characters are allowed in the equation
    char_allowed: determines what characters are chosen
    division_operators: determines how many division operators are allowed

- Converting to latex
    To convert to latex use FUNCTION convert_latex(equation) -> taking any equation as parameter
    from CLASS ReducibleEQGen

--------------------------------------------------------------------------------------------------------------

"""

# ====================================================
# > IMPORTS
# ====================================================
import json
import urllib.request

# Accessing the proper project, since the website has more
_PROJECT = 'equation_generator'

# API Link
_API = 'inc/api.php?'

# Full source
_SOURCE = "http://dreamaboutnow.com/projects/{0}/{1}".format(_PROJECT, _API)


# ===================================================
# > CLASSES
# ====================================================
class EQGeneratorLITE():
    def __init__(self, source=_SOURCE):
        """
        Initialize all the necessary data to make the other functions work in the class
        :param source: Link to the websites API 
        """
        self.status = False
        self.url = source
        try:
            self.response = urllib.request.urlopen(self.url)
            self.status = True
        except ReferenceError:
            self.status = False
            raise ValueError("Couldn't request webpage " + self.url)

    def generate(self, n_gen,
                 difficulty=(2, 4),
                 exponent=(1, 2),
                 numbers=(2, 12),
                 parentheses=(1, 2),
                 parentheses_exponent=(1, 2),
                 exponent_chance=50,
                 char_amount=(1, 3),
                 char_allowed=(),
                 division_operators=(1, 5),
                 unique=True,
                 reducible=True):
        """
        This function are used to generate multiple equations
        :type int     :param n_gen: how many equations should be generated
        :type tuple   :param difficulty: (min n, max n)
        :type tuple   :param exponent: min n, max n)
        :type tuple   :param numbers: (min n, max n)
        :type tuple   :param parentheses: (min n, max n)
        :type tuple   :param parentheses_exponent: (min n, max n)
        :type int     :param exponent_chance: = n
        :type tuple   :param char_amount: = (min n, max n)
        :type tuple   :param char_allowed: = ['a','b'.....]
        :type tuple   :param division_operators: = (min n, max n)
        :type boolean :param unique: This ensures that all equations are unique
        :type boolean :param reducible: This ensures that all equations are reducible
        :return: list of all the equations
        """
        if n_gen > 1000:
            raise ValueError("You are only allowed to generate 1000 equations per api call.")

        # Converting the tuple to a string
        char_allowed = ''.join(str(c) for c in char_allowed)
        if unique:
            unique = '1'
        else:
            unique = '0'

        if reducible:
            reducible = '1'
        else:
            reducible = '0'

        # Creating a list to easily communicate with the api
        link = ['function=multi_generate',
                'difficulty_min=' + str(difficulty[0]),
                'difficulty_max=' + str(difficulty[1]),
                'exponent_min=' + str(exponent[0]),
                'exponent_max=' + str(exponent[1]),
                'numbers_min=' + str(numbers[0]),
                'numbers_max=' + str(numbers[1]),
                'parentheses_min=' + str(parentheses[0]),
                'parentheses_max=' + str(parentheses[1]),
                'parentExponent_min=' + str(parentheses_exponent[0]),
                'parentExponent_max=' + str(parentheses_exponent[1]),
                'parentExponent_chance=' + str(exponent_chance),
                'variable_min=' + str(char_amount[0]),
                'variable_max=' + str(char_amount[1]),
                'variable_string=' + char_allowed,
                'division_min=' + str(division_operators[0]),
                'division_max=' + str(division_operators[1]),
                'generate=' + str(n_gen),
                'unique=' + str(unique),
                'reducible=' + str(reducible)]

        api_link = self.url + ''.join(str(object + '&') for object in link)[:-1]
        self.response = urllib.request.urlopen(api_link)
        return json.loads(self.response.read().decode())

    def convert_latex(self, equation):
        if '/' in equation:
            equation = equation.split('/')
            pos = 0
            latex_equation = ''
            for x in equation:
                if not pos:
                    latex_equation += '\\frac{' + x + '}'
                    pos = 1
                elif pos:
                    latex_equation += '{' + x + '}'
                    pos = 0
            return latex_equation
        else:
            return equation





