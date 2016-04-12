

# find_hipotenuse; Declaration
from math import sqrt
def find_hypotenuse(a,b):
    a_squared = a*a
    b_squared = b*b
    leg_sum = a_squared+b_squared
    return sqrt(leg_sum)

leg1=23
leg2=10

hypotenuse = find_hypotenuse(leg1,leg2)
print hypotenuse

print find_hypotenuse(100,100)
print find_hypotenuse(10.5,5.0)
print find_hypotenuse(45,25)


def print_name(name):
    print 'person name:' + name


print_name('Angel')