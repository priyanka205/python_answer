#  Write a function for checking the speed of drivers. 
#  This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one
#  demerit point and print the total number of demerit points. For example, if the speed is 80, 
#  it should print: “Points: 2”.
# If the driver gets more t
def speed_check(speed):
    if speed<70:
        print("OK")
    elif speed>70:
        demerit_points = int((speed - 70)/5)
        if demerit_points>12:
            print("License Suspended.")
        else:
            print(demerit_points)

speed_check(112)