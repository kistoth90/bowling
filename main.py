def CalculateScore2(input):
    total_arr = []
    arr_input = input.split(" ")

    arr = validate_input(arr_input)
    if arr:
        return arr
    
    for i, frame in enumerate(arr_input):
        arr_input[i] = list(frame)

    for i, frame in enumerate(arr_input[:10]):
        for score in frame:
            if score.isdigit():
                total_arr.append(int(score))
            elif score == 'x':
                total_arr.append(10)
                got = 0
                while 2 > got:
                    for x, x_frame in enumerate(arr_input[i+1:]):
                        for y in x_frame:
                            if y == 'x':
                                total_arr.append(10)
                                got += 1
                            elif y == '/':
                                total_arr.append(10-total_arr[-1])
                                got += 1
                            elif y.isdigit():
                                total_arr.append(int(y))
                                got += 1
                            if got == 2:
                                break
                        if got == 2:
                            break
            elif score == '/':
                total_arr.append(10-total_arr[-1])
                got = 0
                while 1 > got:
                    for x, x_frame in enumerate(arr_input[i+1:]):
                        for y in x_frame:
                            if y == 'x':
                                total_arr.append(10)
                                got += 1
                            elif y.isdigit():
                                total_arr.append(int(y))
                                got += 1
                            if got == 1:
                                break
                        if got == 1:
                            break

    return sum(total_arr)

def validate_input(input):
    err = []
    if len(input) < 10 or len(input) > 12:
        err.append("The length of the input not valid. The frames must be between 10 and 12.")

    return err