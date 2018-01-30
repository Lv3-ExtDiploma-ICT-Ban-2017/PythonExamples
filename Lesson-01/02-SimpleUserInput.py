"""02-SimpleUserInput.py: lets do some loops 'n' that"""

# lets grab some variables
counter = 1  # Lets count the loop
total = 1  # and keep track of a total
target = input("Please enter a number: ")  # And were gonna loop this many times

while counter < int(target):  # This is funky, were gonna keep on going while the counter is less than the target
    # So you notice the int(), this is called casting. Specifically explicit casting, this will change "5" into 5.
    # Isnt that fun
    total = total * counter  # Some maths stuff
    counter += 1  # Then we add 1 to the variable counter, this is using the += operator.
    print("c:", counter, "t:", total)  # And then were gonna tell the user what we have done
