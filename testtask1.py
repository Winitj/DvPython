

import re

docs = [
    "asf dob: 1/5/1991 in tech",
    "DOB 5/5/1991 and educ: 1/6/2010",
    "hi I am good in python. my date of birth is 6/5/2005",
    "edu: 1/2/2008 and DOB 5/8/1991 and education2 1/6/2010",
    "skill master overall. my birth 7/02/22"
]

birthdate_pattern = re.compile(r'(?:dob|DOB|birth).*?(\b\d{1,2}/\d{1,2}/\d{2,4}\b)')

for doc in docs:
    matches = birthdate_pattern.findall(doc)
    if matches:
        print("Birthdates in {}: {}".format(doc, ", ".join(matches)))
