class Fun:
    a = 10  # that is class variable
    b = 20


c = Fun()
d = Fun()

c.value = 30  # that is instance variable
d.value = 40

print(c.value, d.value)
