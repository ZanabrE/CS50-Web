# Call a functions from another file 
# that needs to be imported.
from functions import square

for i in range(10):
    # f stands for formatted string literal - denotes the an f-string
    print(f'The square of {i} is {square(i)}')