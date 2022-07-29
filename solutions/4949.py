while True:
    data = input()
    if data == '.':
        break
    bracket = []
    check = True
    for i in data:
        if i == '(':
            bracket.append(i)
        elif i == '[':
            bracket.append(i)
        elif i == ')':
            if len(bracket) == 0 or bracket[-1] != '(':
                check = False
                break
            else:
                del bracket[-1]
        elif i == ']':
            if len(bracket) == 0 or bracket[-1] != '[':
                check = False
                break
            else:
                del bracket[-1]

    if len(bracket) != 0:
        check = False
    if check:
        print("yes")
    else:
        print("no")
