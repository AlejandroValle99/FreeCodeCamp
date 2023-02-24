def arithmetic_arranger(problems, *ans):
    if len(problems)>5:
        return "Error: Too many problems."

    Pl = ""
    Sl = ""
    Tl = ""
    Cl = ""
 
    for problem in problems:
        Sep_problems=problem.split(" ")

       # print (Sep_problems[1])
  
        operator=Sep_problems[1]    
        num_1=Sep_problems[0]
        num_2=Sep_problems[2]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        if num_1.isnumeric() is False or num_2.isnumeric() is False:
            return "Error: Numbers must only contain digits."

        if operator == "+":
            Result= int(num_1) + int(num_2)
        elif operator == "-":
            Result= int(num_1) - int(num_2)

    
        if len(num_1) > 4 or len(num_2) > 4:
            return "Error: Numbers cannot be more than four digits."

    
        longest_num = max(len(num_1),len(num_2))
        width= longest_num + 2


        # Ln1 = f"{num_1:>{width}}"
        # Ln2 = operator + f"{num_2:>{width-1}}"
        # dashes = "-" * width

        Pl += f"{num_1:>{width}}" + (" " * 4)
        Sl += operator + f"{num_2:>{width-1}}" + (" " * 4)
        Tl += "-" * width + (" " * 4)


        if ans:
            Cl += f"{Result:>{width}}" + (" "*4)
            output = f"{Pl.rstrip()}\n{Sl.rstrip()}\n{Tl.rstrip()}\n{Cl.rstrip()}"
            

        else:
            output = f"{Pl.rstrip()}\n{Sl.rstrip()}\n{Tl.rstrip()}"


        # try:
        #     arr_problems[0] += (' ' * 4) + Ln1
        # except IndexError:
        #     arr_problems.append(Ln1)

        # try:
        #     arr_problems[1] += (' ' * 4) + Ln2
        # except:
        #     arr_problems.append(Ln2)


    # output = f"{arr_problems[0]}\n{arr_problems[1]}"

    
    return output

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))