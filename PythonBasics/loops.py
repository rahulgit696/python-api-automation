
greetings = "Good Morning"

if greetings == "Morning":
    print("Passed")
else:
    print("Failed")

value = [1, 2, 4, 6, 8, 9]

for i in value:
    print(i)

# sum of first natural numbers

result = 0
for j in range(1, 6):  # range(i, j) -> i to j-1
    result = result + j
print(result)


# For loop in python have by default increment value by 1
# To increment the value by 2 or any other number we need to give the value as third parameter

for k in range(1, 10, 3):
    print(k)
print("=======================================================")
# While loops: Runs until the condition is not satisfied

new_value = 10

while new_value > 1:
    if new_value == 9:
        new_value = new_value - 1
        continue
    if new_value == 3:
        break
    print(new_value)
    new_value = new_value - 1