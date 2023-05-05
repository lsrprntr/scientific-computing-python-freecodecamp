#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
#No imports allowed for this exercise

def add_time(start, duration,days=None):
    time,MM = start.split()
    hour,min = time.split(":")
    addhour,addmin = duration.split(":")
    dayadd=0

    #mins
    newmin = int(min)+int(addmin)
    if newmin >=60:
        hour = int(hour)+1
    newmin = (newmin)%60
    if newmin == 0:
        newmin = "00"
    elif newmin < 10:
        newmin = "0"+str(newmin)
    
    #hours
    newhour = int(hour)+int(addhour)
    if newhour >= (12-int(hour)): #AM/PM switch and days elapsed calc
        dayadd = (newhour + (12 if MM == "PM" else 0))//24
        switch = newhour//12%2
        if switch == 1:
            if MM == "AM":
                MM = "PM"
            else:
                MM = "AM"

    newhour = (newhour)%12
    if newhour == 0:
        newhour = "12"

    #days of week
    if days != None:
        week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        day = week[(week.index(days.title())+dayadd)%7]
    
    #days added text
    if dayadd == 1:
        dayadd = "(next day)"
    elif dayadd >=1:
        dayadd = f"({dayadd} days later)"

    #return format
    if days != None:
        if dayadd == 0:
            return f"{newhour}:{newmin} {MM}, {day}"
        return f"{newhour}:{newmin} {MM}, {day} {dayadd}"

    if dayadd == 0:
        return f"{newhour}:{newmin} {MM}"
    return f"{newhour}:{newmin} {MM} {dayadd}"
