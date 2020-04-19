
                                # There are three numeric types in Python:

x = 5
print(type(x))                  # First numeric type is int. int mean integer/without decimal.

y = 5.3
print(type(y))                  # Second numeric type is float. float mean decimal number.

z = 7j
print(type(z))                  # Third numeric typ is complex. Complex numbers are written with a "j"
                                # ...as the imaginary part.
                                # What is the imaginary part? Let's first examine this.

t = 15+3j
print(type(t))

print(t.imag)                   # imag returns the imaginary of the number. So '3j'

print(t.real)                   # real returns the real of the number. So '15'

print(t.conjugate())            # conjugate returns the self of the complex number. So '15+3j'.

x = 5
y = 5.49
z = 5.55
p = 5.55
t = 15+3j

print(float(x))                 # We can convert an integer to a decimal number.
print(int(y))                   # We can convert a decimal to an integer number.
print(int(z))                   # Here, 5.55 turns 5 to an integer with print(int(z)).
print(round(p))                 # Here, 5.55 turns 6 to an integer with round() method.
                                # The float number returns to the nearest integer.

#print(float(t))
#print(int(t))                  # Complex numbers can't be converted to integers or decimal numbers.

                                # We can do mathematical operations in python.
a = 4
b = 3
c = 8
d = 9
e = 16
f = 27



print(a + b)
print(a - b)
print(b - a)
print(d * b)
print(f / b)                    # If we use a single /, the result is decimal.
print(f // b)
print(3 * b)
print((f + b / b))              # The priority of mathematical operations is also valid in Python. Result = 28.0
print((f + b) / b)              # Result = 10.0
print(a ** b)                   # Result = 4 * 4 * 4 = 64

print(max(a,b,c,d,e,f))         # Returns the largest number. Result = f = 27
print(min(a,b,c,d,e,f))         # Returns the largest smallest number. Result = b = 3

Total = [a,b,c,d,e,f]           # This function adds up all the numbers in an index.
print(sum(Total))
print(sum(Total,10))            # This function takes two arguments.
























