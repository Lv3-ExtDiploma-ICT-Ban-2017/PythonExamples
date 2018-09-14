"""01-ranging.py"""

# One argument, for numbers 0 to 5
for i in range(6):
    print(i)

# Two arguments, for numbers 2 to 7
for i in range(2, 8):
    print(i)

# Three arguments, 1 to 10 in steps of 2
for i in range(1, 10, 2):
    print(i)

# Three arguments 10 to 0 in steps of -2
for i in range(10, 0, -2):
    print(i)

days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
for i in range(0, len(days)):
    print(days[i])

for i in range(len(days)-1,-1,-1):
    print(days[i])
