# Def as define the function.
def square(x):
    return x * x

for i in range(10):
    # f stands for formatted string literal - denotes the an f-string
    print(f'The square of {i} is {square(i)}')