
def add_time(s_time, dur, opt=None):
    
    week = {"Sunday":0, "Monday":1, "Tuesday":2,  "Wednesday":3, "Thursday":4, "Friday":5,"Saturday":6}
    
    start_time = s_time.split()
    time = start_time[0].split(":")
    
    hour = time[0]
    min = time[1]
    meridiem = start_time[1]
    
    dur_time = dur.split(":")
    dhour = dur_time[0]
    dmin = dur_time [1]


    fhour = int(hour) + int(dhour)
    fmin = int(min) + int(dmin)
    quotient = 0
    remainder = 0
    days = 0
    
    if fmin >=60:
        fhour += 1
        fmin -= 60
    
    if fmin <10:
        fmin = str(fmin).zfill(2)  

     
    if fhour >=12:
    
        quotient = fhour//12
        remainder = fhour%12 
        fhour = remainder

        if remainder == 0 :
            fhour = 12 


        print(quotient, remainder,  quotient % 2 != 0)

        if (quotient > 0) and (quotient % 2 != 0):
            if meridiem  == "PM":
                meridiem = "AM"

            else:
                meridiem = "PM"

        
        if meridiem == "AM":    
            days = (((quotient-1)//2) + 1)  
    
        else:
            days = (quotient//2)

    # print (days)

    if opt is not None:
        day = opt.capitalize()

        dia_actual = week.get(day)
        dia_futuro = int(dia_actual) + int(days)

        div_mod7 = (dia_futuro/7)

        wholediv = str(div_mod7)
        wholedividend = int(wholediv.split(".")[0])

        whole_mod7 = wholedividend * 7
        remainder7 =  dia_futuro - whole_mod7

        # print(div_mod7)
        # print(wholedividend)
        # print(whole_mod7)
        # print(remainder7)


        for key,value in week.items():
            if value == remainder7:
                dia_final = key

    

    final_time = str(fhour) + ":"

    if days == 1 and opt is None:
        final_time += str(fmin) + f" {meridiem}" + f" (next day)"

    elif days > 1 and opt is None:
        final_time += str(fmin) + f" {meridiem}" + f" ({days} days later)"


    if days == 1 and opt is not None:
        final_time += str(fmin) + f" {meridiem}" + f" {dia_final}" + f" (next day)"

    elif days > 1 and opt is not None:
            final_time += str(fmin) + f" {meridiem}" + f" {dia_final}" + f" ({days} days later)"

    else:
        final_time += str(fmin) + f" {meridiem}"
    


        
    return final_time




print(add_time("2:59 AM", "24:00", "SaturDAY"))