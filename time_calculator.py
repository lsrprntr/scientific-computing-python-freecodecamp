#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
#No imports allowed for this exercise

def add_time(start, duration,days=None):
    time,MM = start.split()
    hour,min = time.split(":")
    addhour,addmin = duration.split(":")

    #mins
    newmin = int(min)+int(addmin)
    if newmin >=60:
        hour = int(hour)+1
    newmin = (newmin)%60
    if newmin == 0:
        newmin = "00"
    
    #hours
    newhour = int(hour)+int(addhour)
    if newhour >= (12-int(hour)): #AM/PM switch calc
        switch = newhour//12%2
        if switch == 1:
            if MM == "AM":
                MM == "PM"
            else:
                MM = "AM"
       
    newhour = (newhour)%12
    
    

    #AM/PM calc
    if int(addhour)//12%2==0:
        days =1
    
    #format
    print("Start time", start,"Add",duration)
    print("Newtime", newhour,":",newmin,MM)
    print("Day result", days)
    print("Days elapsed",days)
    return

add_time("1:01 PM","23:59")
