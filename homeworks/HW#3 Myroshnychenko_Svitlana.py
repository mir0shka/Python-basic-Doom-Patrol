# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
#140245777506352
print(id(str_b))
#140245776007600
print(id(set_c))
#140245775861792
print(id(lst_d))
#140245776270336
print(id(dict_e))
#140245776728640

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append([4, 5])
print(id(lst_d))
#140463449793536


# 3. Define the type of each object from step 1.
print(type(int_a))
#<class 'int'>
print(type(str_b))
#<class 'str'>
print(type(set_c))
#<class 'set'>
print(type(lst_d))
#<class 'list'>
print(type(dict_e))
#<class 'dict'>

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
#True
print(isinstance(str_b, str))
#True
print(isinstance(set_c, set))
#True
print(isinstance(lst_d, list))
#True
print(isinstance(dict_e, dict))
#True

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(5, 6))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(5, 6))

# 7. By using keyword arguments into the curly braces.
print("Anna has {a} apples and {b} peaches.".format(a="5", b="6"))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(5, 6))

# 9. With f-strings and variables
a = 5
b = 6
print(f"Anna has {a} apples and {b} peaches.")

# 10. With % operator
a = 5
b = 6
print("Anna has %.d apples and %.d peaches." % (a, b))

# 11*. With variable substitutions by name (hint: by using dict)
a = 5
b = 6
dict1 = {'first': a, 'second': b}
print("Anna has %(first).d apples and %(second).d peaches." % dict1)

#Comprehensions:

# 12. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)


#13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)


# 14. Convert (3) to dict comprehension.
dict_comprehension = {num: num**2  for num in range(1, 11) if num% 2 == 1}
print(dict_comprehension)


# 15*. Convert (4) to dict comprehension.
dict_comprehension = {num: num**2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension)


# 16. Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
print(d)


# 17*. Convert (6) to regular for with if-else.
d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)


#Lambda:
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(1, 5))
print(foo(7, 3))

# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x > z:
        return z
    else:
        return y
print(foo(1, 5, 6))
print(foo(7, 3, 4))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort_1 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort_1)

# 23*. Raise each list number to the corresponding number on another list: (возвести число из 1 списка на соотв число из 2 списка)
list_A = [2, 3, 4]
list_B = [5, 6, 7]
raising_result = [a ** b for a, b in zip(list_A, list_B)]
print(raising_result)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
import functools
print(functools.reduce(lambda x, y: x + y, lst_to_sort))
#164


# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
new_lst_to_sort = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_lst_to_sort)


# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
lst_2 = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_2)


# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda element:element in list_1, list_2)))