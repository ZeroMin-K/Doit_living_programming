import re

number = 'My number is 511223-1****** yours is 521012-2******'
print(re.findall('\d{6}', number))
