import math

def square(side):
    area = side ** 2
    return math.ceil(area)

result = square(4.3)
print(result) 
