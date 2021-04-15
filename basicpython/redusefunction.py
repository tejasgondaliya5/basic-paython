from functools import *

a = [10 , 20 , 30 , 40 , 50]

x = reduce(lambda n , m : n+m , a)  # reduse is return always singale value

print(x)
print(type(x))
