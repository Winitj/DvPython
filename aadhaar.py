import re

pattern = '^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$'
test_string = '2001 0000 0000'
result = re.match(pattern, test_string)

if result:
  print("Search successful it is a Aadhar number.")
else:
  print(" it is not a Aadhar number .")