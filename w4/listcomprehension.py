def square(x):
    return(x*x)

def iseven(x):
    return(x%2 == 0)


# list comprehension: [map_fn generators filters]
pythagorean_triples = [(x,y,z) for x in range(1,100) for y in range(x,100) for z in range(y,100) if square(x) + square(y) == square(z)]

even_squares = [square(x) for x in range(101) if iseven(x)]

# print(even_squares)
print(pythagorean_triples)