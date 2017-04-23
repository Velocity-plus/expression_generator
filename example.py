from generate_equations import generator_lite_api

EQGen = generator_lite_api.EQGeneratorLITE()


# If you need to read the documentation
doc = 0
if doc:
    help(generator_lite_api)


""" Generation example"""
generated = EQGen.generate(n_gen=100,
                 difficulty=(2, 3),
                 exponent=(0, 3),
                 numbers=(2, 12),
                 parentheses=(2, 2),
                 parentheses_exponent=(1, 2),
                 exponent_chance=50,
                 char_amount=(2, 3),
                 char_allowed=('x', 'y'),
                 division_operators=(0, 1),
                 unique=True,
                 reducible=True)

print(generated)
for equation in generated:
    print(equation)
