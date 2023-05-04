def arithmetic_arranger(problems,req=False):#list of problems given, requests for the answer default False
    if len(problems)>5:raise "Error: Too many problems."
    tops,bots,totals=list()
    print(tops,bots,totals)
    for i in problems:
        top,sign,bot = i.split()
        if sign not in "+-":
            raise "Error: Operator must be '+' or '-'."
        try:
            if sign == "+":
                total = int(top)+int(bot)
            else:
                total = int(top)-int(bot)
        except:
            raise "Error: Numbers must only contain digits."
        #format to lists
        tops.append(top)
        bots.append(bot)
        totals.append(total)
        
    return "AAA"

arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "123 + 49"],True)
