print("Hello world1")
a = 0

if a == 0:
    print("a is zero")
else:
    print("a is not zero")


# list
my_list = [0, 1, 2, 3]
# for each loop
for item in my_list:
    print(item)

# looping with index
for index, value in enumerate(my_list):
    print(str(index) + "," + str(value))

#dictionaries
dictionary = {"first_name": "Ramiz", "last_name": "Raja"}
for key in dictionary:
    print(dictionary[key])

#append data to new array
newList = []
for key in dictionary:
    newList.append(dictionary[key])

print(newList)

# functions
def sum(a, b):
    return a + b

print(sum(1, 2))

#generators to deal with large data sets
def next_even():
    n = 0
    while True:
        yield n
        n += 2

print()
print("First 5 even numbers")
#get the reference to generator so that this reference maintains state and not reset
even_generator = next_even()
for i in range(5):
    print(next(even_generator))
