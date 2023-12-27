"""
#ITTRATIVE


import json
import re

def identify_and_validate_keys(data, patterns):
    identified_keys = []
    stack = [(data, '')]

    while stack:
        obj, current_key = stack.pop()

        if isinstance(obj, list):
            for i, item in enumerate(obj):
                stack.append((item, f'{current_key}[{i}]'))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    stack.append((v, nested_key))
                elif isinstance(v, str):
                    for pattern_type, pattern in patterns.items():
                        if pattern.match(v):
                            validity = 'valid' if validate_number(v, pattern) else 'invalid'
                            identified_keys.append((nested_key, v, pattern_type, validity))

    return identified_keys

def validate_number(number, pattern):
    return bool(pattern.match(number))

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Compile patterns outside the loop
""" """
aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')
""" """

aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]\d{1}$')
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]\d{2}[Z][0-9A-Z]{1}$')

patterns = {'Aadhar': aadhar_pattern, 'PAN': pan_pattern, 'GST': gst_pattern}

# Identify and validate keys containing Aadhar, PAN, and GST numbers
identified_keys = identify_and_validate_keys(data, patterns)

# Display the identified and validated keys
for key, value, pattern_type, validity in identified_keys:
    print(f"{key}: {value} is {validity} for {pattern_type}")

    """
"""
import json
import re

def identify_and_validate_keys(data, patterns):
    identified_keys = []
    stack = [(data, '')]

    while stack:
        obj, current_key = stack.pop()

        if isinstance(obj, list):
            for i, item in enumerate(obj):
                stack.append((item, f'{current_key}[{i}]'))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    stack.append((v, nested_key))
                elif isinstance(v, str):
                    for pattern_type, pattern in patterns.items():
                        if pattern.match(v):
                            validity = 'valid' if validate_number(v, pattern) else 'invalid'
                            identified_keys.append((nested_key, v, pattern_type, validity))

    return identified_keys

def validate_number(number, pattern):
    return bool(pattern.match(number))

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Compile patterns outside the loop
aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')  # Adjusted PAN pattern
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')

patterns = {'Aadhar': aadhar_pattern, 'PAN': pan_pattern, 'GST': gst_pattern}

# Identify and validate keys containing Aadhar, PAN, and GST numbers
identified_keys = identify_and_validate_keys(data, patterns)

# Display the identified and validated keys
for key, value, pattern_type, validity in identified_keys:
    print(f"{key}: {value} is {validity} for {pattern_type}")
"""

"""

import json
import re

def identify_and_validate_keys(data, patterns):
    identified_keys = []
    stack = [(data, '')]

    while stack:
        obj, current_key = stack.pop()

        if isinstance(obj, list):
            for i, item in enumerate(obj):
                stack.append((item, f'{current_key}[{i}]'))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    stack.append((v, nested_key))
                elif isinstance(v, str):
                    for pattern_type, pattern in patterns.items():
                        if pattern.match(v):
                            validity = 'valid' if validate_number(v, pattern) else 'invalid'
                            identified_keys.append((nested_key, v, pattern_type, validity))

    return identified_keys

def validate_number(number, pattern):
    return bool(pattern.match(number))

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Compile patterns outside the loop
aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')  # Adjusted PAN pattern
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')

patterns = {'Aadhar': aadhar_pattern, 'PAN': pan_pattern, 'GST': gst_pattern}

# Identify and validate keys containing Aadhar, PAN, and GST numbers
identified_keys = identify_and_validate_keys(data, patterns)

# Display the identified and validated keys
for key, value, pattern_type, validity in identified_keys:
    print(f"{key}: {value} is {validity} for {pattern_type}")
"""

import json
import re

def identify_and_validate_keys(data, patterns):
    identified_keys = []
    stack = [(data, '')]

    while stack:
        obj, current_key = stack.pop()

        if isinstance(obj, list):
            for i, item in enumerate(obj):
                stack.append((item, f'{current_key}[{i}]'))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    stack.append((v, nested_key))
                elif isinstance(v, str):
                    for pattern_type, pattern in patterns.items():
                        if pattern.match(v):
                            validity = 'valid'if validate_number(v, pattern)else 'invalid'
                            identified_keys.append((nested_key, v, pattern_type, validity))

    return identified_keys

def validate_number(number, pattern):
    return bool(pattern.match(number))

json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'


with open(json_file_path, 'r') as file:
   
    data = json.load(file)

# Compile patterns outside the loop
aadhar_pattern = re.compile(r'^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$')
pan_pattern = re.compile(r'^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$') 
gst_pattern = re.compile(r'^([0-3]{1}[0-9]{1}|[9]{1}[8-9]{1})[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}([1-9]|[A-Z]){1}$')

patterns = {'Aadhar': aadhar_pattern, 'PAN': pan_pattern, 'GST': gst_pattern}


identified_keys = identify_and_validate_keys(data, patterns)


output = ""
for key, value, pattern_type, validity in identified_keys:
    output += f"{key}: {value} is {validity} for {pattern_type}\n"
    

print(output) 

#14401 function calls (14243 primitive calls) in 0.059 seconds  54.321% difference   --Nested  used stack
#8142 function calls (7984 primitive calls) in 0.031 seconds    62.2222% difference  --Flat




