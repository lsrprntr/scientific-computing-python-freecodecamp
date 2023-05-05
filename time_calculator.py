#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
#No imports allowed for this exercise

def add_time(start, duration,day=None):
    time,MM = start.split()
    hour,min = time.split(":")
    addhour,addmin = duration.split(":")

    #mins
    newmin = int(min)+int(addmin)
    if newmin >=60:
        hour = int(hour)+1
    newmin = (newmin)%60
    
    #hours
    newhour = int(hour)+int(addhour)
    if newhour >=12:
        days = 1
    newhour = (newhour)%12
    
    print(newhour)
    print(newmin)

    #AM/PM calc
    if int(addhour)//12%2==0:
        print("switch ampm")
    
    #format

    return

add_time("12:20 PM","2:40")
