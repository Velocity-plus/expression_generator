# Reducible Equation Generator
A library that can generate equations that can be reduced 


====
Documentation:
====

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
