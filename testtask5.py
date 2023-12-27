

import re

pattern = '^[1-9]{1}[0-9]{2}\s[0-9]{3}$'
test_string = input("Enter your value: ")
result = re.match(pattern, test_string)

if result:
  print("Search successful it is a pin.")
else:
  print("Search unsuccessful it is not a pin.")  