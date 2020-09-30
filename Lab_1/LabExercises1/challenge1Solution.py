# Generate a sequence of int numbers in the pattern 0, 2, 4 …. up
# to 20 inclusive and display the numbers on the screen.

x = 0
while x <= 20:
    print(x)
    x += 2

# Allow the user to enter a string, and then print out each letter
# in the string one at a time on a separate line.

a = input('Enter some text: ')
x = 0
while x < len(a):
    print(a[x])
    x += 1

# As above, but print out the letters in the string in reverse order.

a = input('Enter some text: ')
x = -1
while x >= -(len(a)):
    print(a[x])
    x -= 1

# Starting with the initial value 0 and 1, generate a Fibonacci sequence.
# Each element in a Fibonacci sequence is the sum of the two previous
# elements e.g. 0, 1, 1, 2, 3, 5, 8 ……
# Allow the user to specify how many elements should be generated.

x = int(input('How many elements? '))
x -= 2 # There are 2 elements already ...
x1 = 0
x2 = 1
y = 0
print(x1)
print(x2)

while y < x:
    x3 = x1 + x2
    print(x3)
    x1 = x2
    x2 = x3
    y += 1
