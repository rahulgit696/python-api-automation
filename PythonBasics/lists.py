# List is data type that allows multiple values and can be different data types
# Lists are mutable: can be changed

values = [1, 2, 3, "Rahul", 4, 5]

print(values[0])

print(values[-1])  # Pointing to last index of lists or array

print(values[2:4])  # slicing and printing from source index to destination index

values.insert(4, "Badoni")  # Inserting any data type by providing them index number of it
print(values)

values.append("End of List")  # Append: Adding any data type to the last index of the lists
print(values)

values[3] = "RAHUL"
print(values)
