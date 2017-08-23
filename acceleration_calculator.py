# Create a function that calculates acceleration given
# Initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is:
# a = (v2-v1)/(t2-t1)

# Solution (Python 2.6)
def accel_calc(v1, v2, t1, t2):
    return float(v2 - v1) / float(t2 - t1)

print(accel_calc(0, 10, 0, 20))

