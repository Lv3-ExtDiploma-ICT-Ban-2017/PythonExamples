"""02-SimpleUserInput.py: lets do some loops 'n' that"""

# lets grab some variables
counter = 1  # Lets count the loop
total = 1  # and keep track of a total
# And were gonna loop this many times:
target = 0  # we put this here to keep it in "scope"
while True:
    try:
        target = int(input("Please enter a number: "))  # Hardcoding is no fun so lets ask the user for a number
        # So you notice the int(), this is called casting. Specifically explicit casting, this will change "5" into 5.
        # Isnt that fun
    except ValueError:  # this shows that the user has done something wrong
        print("ERROR: I dont think you know what a number is, please try again!!!")
        continue  # This tells the loop to continue and ignore everything else in the block
    break  # This code will only be called if the continue does not get hit, IE, the input is correct

while counter < target:  # This is funky, were gonna keep on going while the counter is less than the target
    total = total * counter  # Some maths stuff
    counter += 1  # Then we add 1 to the variable counter, this is using the += operator.
    print("c:", counter, "t:", total)  # And then were gonna tell the user what we have done
