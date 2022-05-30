
from itertools import product

def multiply_and_greet(*integers,**attributes):
    product = 1
    for x in integers:
        product *= x
    print(f"Hello {attributes['name']} from {attributes['country']} your score is {product}")
    