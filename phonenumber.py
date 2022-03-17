def isPhoneNumber(text):
    if len(text) != 12:
        return print("This is not a phone number.")
    for i in range(0,3):
        if not text[i].isdecimal():
            return print("This is not a phone number.")
    if text[3] != '-':
        return print("This is not a phone number.")
    for i in range(4, 7):
        if not text[i].isdecimal():
            return print("This is not a phone number.")
    if text[7] != '-':
        return print("This is not a phone number.")
    for i in range(8, 12):
        if not text[i].isdecimal():
            return print("This is not a phone number.")
    return print("This is a phone number")

    