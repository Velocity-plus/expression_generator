Reducible Equation Generator
===================== 
Version 1.0.0
last update *23-04-2017*


------------------------

>#### Table of contents
> - **<a href="#introduction">Introduction</a>**
> - **<a href="#documentation">Documentation</a>**
> - <a href="#getting-started">Getting started</a>


Introduction
-----------------------------
   This project contains code to supposedly generate mathematical reducible equations.
   It is not guaranteed that all equations generated are reducible, since they are randomly generated.
   This flaw can be solved by setting the correct parameter in 'FUNCTION <generate>' from 'CLASS ReducibleEQGen'
   
  To generate random equations there are a lot of variables and decision factors that plays a role
  in the generation of the equations.

Documentation
---------------------
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
