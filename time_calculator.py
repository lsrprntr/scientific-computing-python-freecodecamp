#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
#No imports allowed for this exercise

def add_time(start, duration,day=None):
    time,MM = start.split()
    hour,min = time.split(":")
    addhour,addmin = duration.split(":")

    #new time calc
    newhour = (int(hour)+int(addhour))%12
    newmin = (int(min)+int(addmin))%60

    print(newhour)

    print(newmin)

    #AM/PM calc
    if int(addhour)//12%2==0:
        print("switch ampm")
    
    #format
    
    return

add_time("2:20 PM","2:40")
