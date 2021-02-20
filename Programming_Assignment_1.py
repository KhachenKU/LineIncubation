# Recieve input from user
# Assume that the user input like an example
# For example "2 4 88 2 78 88 34"
input_stream = input()
# Change type of the input to integer
input_stream = [int(x) for x in input_stream.split()]

# Initial variable
count = {} # Declare "count" variable for collect the count of a integer

# Iterate for count the number of each elenemt
for element in input_stream:
    if element not in count:
        count[element] = 1
    else:
        count[element] += 1

# Check for duplicated
# Then print out the number that duplicated
for key, value in count.items():
    if value > 1:
        print(key)