from functools import reduce


# multiply func will take two elements and multiply together
# product func will take an iterable and apply the function across the list

multiply = lambda a, b: a*b
product = lambda x: reduce(multiply, x)

# step 1: 2*5 = 10
# step 2: 10*8 = 80
# step 3: 80*7 = 560
# step 4: 560*-1 = -560
# step 5: -560*-2 = 1120

result = product([2,5,8,7,-1,-2])
print(result)
