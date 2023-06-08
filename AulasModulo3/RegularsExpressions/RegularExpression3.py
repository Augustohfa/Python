# caractere pipe '|'
# Utilizado como separador 'ou' no Regex
# A Expressão regular r'Batman|Tina fey' - corresponde
# ou a 'Batman' ou a 'Tina Fey'
import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')

print(mo1.group())


mo2 = heroRegex.search(r'Tina Fey and Batman')
print(mo2.group())
