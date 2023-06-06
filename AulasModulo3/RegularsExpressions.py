def isPhoneNumber(text):
    if len(text) != 11:
        return False
    try:
        int(text)
    except ValueError:
        return 'Not a number'
    else:
        return True


number = '48988189dds'

print(isPhoneNumber(number))
