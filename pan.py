

import re

pattern = '^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$'
test_string = 'AAEAR5531N'
result = re.match(pattern, test_string)

if result:
  print("Search successful it is a pancard.")
else:
  print("Search unsuccessful it is not a pancard.")  




