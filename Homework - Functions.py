# Exercises 1:

def my_function(a=1, b=5, c=-3, d='abc', e=[12, 56, 'cad']):
    return a + b - c

print(my_function(1, 5, 3))

def my_function():
    return 0

print(my_function())

def my_function(a=2, b=4, c='abc', param_1=2):
    return a + b

print(my_function(2, 4))

# Exercises 2:

def get_number(n):
    if n == 0:
        return 0
    return n + get_number(n - 1)

print(get_number(9))

def my_even(n):
    if n==0:
        return 0
    if not n % 2 == 0:
        return my_even(n-1)
    else:
        return n + my_even(n-1)

print(my_even(10))

def my_odd(n):
    if n==0:
        return 0
    if not n % 2 == 1:
        return my_odd(n-1)
    else:
        return n + my_odd(n-1)

print(my_odd(16))

# Exercises 3:

try:
    value = int(input("value = "))
    print("Value is a integer")
except:
    print("0")
finally:
    print("The End")