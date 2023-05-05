#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
#No imports allowed for this exercise

def add_time(start, duration,day=None):
    hours = [1,2,3,4,5,6,7,8,9,10,11,12]
    hour,min = start.split(":")
    min,MM = min.split()
    addhour,addmin = duration.split(":")


    print(hours[16%12])
    
    
    return

add_time("10:20 PM","23:22")
