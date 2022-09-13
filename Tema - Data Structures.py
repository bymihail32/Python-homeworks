# Declararea listei cu elementele continute:

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print("My list:", my_list)

# Lista ordonata ascendent

my_list.sort()

print("List in ascending order:", my_list)

# Lista ordonata descendent

my_list.sort(reverse=True)

print("List in descending order:", my_list)

# Lista cu numerele pare

my_sliced_list = my_list[-2::-2]

print("List of even numbers:", my_sliced_list)

# Lista cu numerele impare

my_sliced_list = my_list[::-2]

print("List of odd numbers:", my_sliced_list)

# Lista cu multipli lui 3

my_sliced_list = my_list[-3::-3]

print("List of multiples of 3:", my_sliced_list)
