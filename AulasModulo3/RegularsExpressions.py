# Considerando numeros tudo aquilo que
# tem 12 34567-8911 12 caracteres
# sendo o 8 '-'
# e tendo seu terceiro numero '9'

def isPhoneNumber(text):
    if len(text) != 14:
        return False
    if text[9] != '-':
        return False
    try:
        int(text)
    except ValueError:
        return 'Not a number'
    if text[4] != '9':
        return False
    if not text[0] == '(' and text[2] == ')':
        return False


# number = '48988189dds'
# print(isPhoneNumber(number))
message = 'Call me at (48)98818-9431. Or call my office (48)99658-0731'

for i in range(len(message)):
    chunk = message[i:i+14]

    if isPhoneNumber(chunk):
        print(f'Fone number in the string is {chunk}')

print('Done')
