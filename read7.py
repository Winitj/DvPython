"""
import json
import re

def identify_and_validate_keys(data, key_type, pattern):
    identified_keys = []

    stack = [(data, '')]

    while stack:
        current_obj, current_key = stack.pop()

        if isinstance(current_obj, list):
            for i, item in enumerate(current_obj):
                stack.append((item, f'{current_key}[{i}]'))
        elif isinstance(current_obj, dict):
            for k, v in current_obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    stack.append((v, nested_key))
                elif isinstance(v, str):
                    match = pattern.match(v)
                    if match:
                        identified_keys.append((nested_key, v, 'valid'))
                    else:
                        identified_keys.append((nested_key, v, 'invalid'))

    return identified_keys

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Precompile regular expressions
aadhar_pattern = re.compile(r'^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$')
pan_pattern = re.compile(r'^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^([0-3]{1}[0-9]{1}|[9]{1}[8-9]{1})[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}([1-9]|[A-Z]){1}$')

# Identify and validate keys containing Aadhar, PAN, and GST numbers


print("Keys containing Aadhar, PAN, or GST numbers:")

for key, value, validity in identify_and_validate_keys(data, 'Aadhar', aadhar_pattern):
    print(f"{key}: {value} is {validity}")

print("Keys containing Aadhar, PAN, or GST numbers:")
for key, value, validity in identify_and_validate_keys(data, 'PAN', pan_pattern):
    print(f"{key}: {value} is {validity}")

print("Keys containing Aadhar, PAN, or GST numbers:")
for key, value, validity in identify_and_validate_keys(data, 'GST', gst_pattern):
    print(f"{key}: {value} is {validity}")

# Repeat similar blocks for PAN and GST
# 12095 function calls (11937 primitive calls) in 0.268 seconds   
# 27359 function calls (27201 primitive calls) in 0.831 seconds
    
    """


import json
import re

def identify_and_validate_keys(data, key_type, pattern):
    identified_keys = []

    stack = [(data, '')]

    while stack:
        current_obj, current_key = stack.pop()

        if isinstance(current_obj, list):
            for i, item in enumerate(current_obj):
                stack.append((item, f'{current_key}[{i}]'))
        elif isinstance(current_obj, dict):
            for k, v in current_obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    stack.append((v, nested_key))
                elif isinstance(v, str):
                    match = pattern.match(v)
                    if match:
                        identified_keys.append((nested_key, v, 'valid'))
                    else:
                        identified_keys.append((nested_key, v, 'invalid'))

                        # Debugging output
                        print(f"Invalid: {nested_key}: {v}")

    return identified_keys

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Precompile regular expressions
aadhar_pattern = re.compile(r'^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$')
pan_pattern = re.compile(r'^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^([0-3]{1}[0-9]{1}|[9]{1}[8-9]{1})[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}([1-9]|[A-Z]){1}$')

# Identify and validate keys containing Aadhar, PAN, and GST numbers
print("Keys containing Aadhar, PAN, or GST numbers:")
for key, value, validity in identify_and_validate_keys(data, 'Aadhar', aadhar_pattern):
    print(f"{key}: {value} is {validity}")

print("Keys containing Aadhar, PAN, or GST numbers:")
for key, value, validity in identify_and_validate_keys(data, 'PAN', pan_pattern):
    print(f"{key}: {value} is {validity}")

print("Keys containing Aadhar, PAN, or GST numbers:")
for key, value, validity in identify_and_validate_keys(data, 'GST', gst_pattern):
    print(f"{key}: {value} is {validity}")
