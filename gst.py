
import re

pattern = '^([0-3]{1}[0-9]{1}|[9]{1}[8-9]{1})[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}([1-9]|[A-Z]){1}$'
test_string = '24AAPFD2680Q1ZT'
result = re.match(pattern, test_string)

if result:
  print("Search successful it is a GST number.")
else:
  print("Search unsuccessful it is not a GST .")