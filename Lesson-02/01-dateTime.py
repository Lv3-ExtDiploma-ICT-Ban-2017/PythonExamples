"""01-dateTime.py: For when a date just wont do"""
import datetime

# So this is something new, we are gonna just grab someone else's code and run with that, Because python

# We can get the current date and time as their varying classes
# We can print them to the console or reference the individual parts (i.e. days or weeks)
today = datetime.date.today()  # 2018-03-13
now = datetime.datetime.now()  # 2018-03-13 15:54:03.366467
print(today, type(today))  # 2018-03-13             <class 'datetime.date'>
print(now, type(now))  # 2018-03-13 15:54:03.366467 <class 'datetime.datetime'>

# We can also do math
datediff1 = datetime.timedelta(days=14)
datediff2 = datetime.timedelta(weeks=3)
timediff1 = datetime.timedelta(hours=4)
# This can store the deltas, this will be used in simple mathematics
print("Two weeks from now is: ", today + datediff1)  # Two weeks from now is:  2018-03-27
print("Three weeks ago was: ", today - datediff2)  # Three weeks ago was:  2018-02-20
print("In 4 hours the time will be : ", now + timediff1)  # In 4 hours the time will be :  2018-03-13 20:05:20.787961
