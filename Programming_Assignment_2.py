import re

# Receive input from the user (only one line of input)
input_stream = input()

# Count the word "LINE MELODY"
COUNT_LINE_MELODY = re.findall("LINE MELODY", input_stream)
print("Number of 'LINE MELODY': " + str(len(COUNT_LINE_MELODY)))

# Count the word "LINE" and "Call"
COUNT_LINE_AND_Call = re.findall("LINE", input_stream) + re.findall("Call", input_stream)
print("Number of 'LINE' and 'Call': " + str(len(COUNT_LINE_AND_Call)))

# Print out the phase "express your feelings" if this phrase appear in the input
express_your_feelings = re.findall("express your feelings", input_stream)
for i in express_your_feelings:
    print(i)

# Reverse each word then print out
tmp1 = input_stream.split()
reverse = []
for i in tmp1:
    if i[-1] == ',' or i[-1] == '.':
        tmp2 = i[:-1]
        reverse.append(tmp2[::-1] + i[-1])
    else:
        reverse.append(i[::-1])
print(" ".join(reverse))