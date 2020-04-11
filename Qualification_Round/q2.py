T = int(input())

for i in range(T):
    case_str = ""
    numbers = list(map(int, [i for i in input()]))
    p_num = 0

    for num in numbers:
        if (num == p_num):
            case_str += str(num)
        elif (num > p_num):
            case_str += "(" * (num - p_num)
            case_str += str(num)
            p_num = num

        else:
            case_str += ")" * (p_num - num)
            case_str += str(num)
            p_num = num


    if(p_num != 0):
        case_str+=")"*(p_num)

    msg = "Case #" + str(i + 1) + ": " + case_str
    print(msg)