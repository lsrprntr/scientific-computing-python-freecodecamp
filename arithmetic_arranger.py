#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def arithmetic_arranger(problems,req=False):#list of problems given, requests for the answer default False
    if len(problems)>5:return "Error: Too many problems." #Error 1

    tops,bots,totals,dashes=[],[],[],[]
    
    for problem in problems:

        top,sign,bot = problem.split()

        if sign not in "+-": #Error 2
            return "Error: Operator must be '+' or '-'."
        try:
            if sign == "+":
                total = int(top)+int(bot)
            else:
                total = int(top)-int(bot)
        except:
            return "Error: Numbers must only contain digits." #Error 3
        if len(top)>4 or len(bot)>4: return print("Error: Numbers cannot be more than four digits.") #Error 4

        #format spacing
        space = max(len(str(top)),len(str(bot)))+2
        top = str(top).rjust(space)
        bot = sign+str(bot).rjust(space-1)
        total = str(total).rjust(space)
        dash = "-"*space

        #add to lists
        tops.append(top)
        bots.append(bot)
        totals.append(total)
        dashes.append(dash)

    #answer check    
    if req == True:
        return f"{'    '.join(tops)}\n{'    '.join(bots)}\n{'    '.join(dashes)}\n{'    '.join(totals)}"
    else:
        return f"{'    '.join(tops)}\n{'    '.join(bots)}\n{'    '.join(dashes)}"

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
