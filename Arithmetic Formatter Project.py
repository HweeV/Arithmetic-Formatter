def arithmetic_arranger(problems, show_answers=False):
    line1 = []
    line2 = []
    dash = []
    answer = []
    result = ''
    digit = '0123456789+- '
    if len(problems) > 5:
        result = 'Error: Too many problems.'
        print(result)
        return result

    else:
        for problem in problems:
            x = problem.split()
            if x[1] == '+' or x[1] == '-':
                pass
            else:
                result = "Error: Operator must be '+' or '-'."
                print(result)
                return result

            if len(x[0]) < 5 and len(x[2]) < 5 :
                pass
            else:
                result = 'Error: Numbers cannot be more than four digits.'
                print(result)
                return result

            for dg in problem:
                if digit.find(dg) != -1 :
                    pass
                else:
                    result = 'Error: Numbers must only contain digits.'
                    print(result)
                    return result

            if x[1] == '+':
                r = int(x[0]) + int(x[2])
            elif x[1] == '-':
                r = int(x[0]) - int(x[2])
            l = (max(len(x[0]),len(x[2]))) + 2
            x[0] = (" "*(l-len(x[0]))) + x[0]
            x[2] = x[1] + (" "*(l-len(x[2])-1)) + x[2]
            r = str(r)
            r = (" "*(l-len(r))) + r     
            d = "-"*l

            line1.append(x[0])
            line2.append(x[2])
            dash.append(d)
            answer.append(r)
        result = "    ".join(line1) +'\n'+"    ".join(line2) +'\n' +  "    ".join(dash) 
        if show_answers==True:
            result = result + '\n' + "    ".join(answer)
        print(result)

    return result
