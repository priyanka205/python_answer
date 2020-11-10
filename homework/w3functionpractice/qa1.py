
# Write a Python function to find the Max of three numbers.
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

def max_of_two(a, b):
    if a > b:
        return a
    if a < b:
        return b
def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b,c))

print(max_of_three(3,9,12))