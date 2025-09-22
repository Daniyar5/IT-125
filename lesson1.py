data_tupe = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tupe:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)

letters.append(numbers.pop(0))

numbers.insert(1, 2)

numbers.sort()

letters.reverse()
letters[1] = 'G'
letters.insert(2, 'r')
letters.remove("k")
letters.remove("T")
letters.remove("C")
del letters[5]
letters[5] = 'n'
del letters[0]

letters = tuple(letters)
numbers = tuple(numbers)

print(f"{letters}\n{numbers}")