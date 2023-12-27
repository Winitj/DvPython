
"""
import json
import re

def identify_key(obj, pattern, current_key=''):
    identified_keys = []

    if isinstance(obj, list):
        for i, item in enumerate(obj):
            identified_keys.extend(identify_key(item, pattern, current_key=f'{current_key}[{i}]'))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            nested_key = f'{current_key}["{k}"]' if current_key else k
            if isinstance(v, (dict, list)):
                identified_keys.extend(identify_key(v, pattern, current_key=nested_key))
            elif isinstance(v, str) and pattern.match(v):
                identified_keys.append((nested_key, v))
    
    return identified_keys

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)


# Identify keys containing Aadhar, PAN, and GST numbers and directly print the output
aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')

print("Keys containing Aadhar numbers:")
for key, value in identify_key(data, aadhar_pattern):
    validity = 'valid' if aadhar_pattern.match(value) else 'invalid'
    print(f"{key}: {value} is {validity}")

print("\nKeys containing PAN numbers:")
for key, value in identify_key(data, pan_pattern):
    validity = 'valid' if pan_pattern.match(value) else 'invalid'
    print(f"{key}: {value} is {validity}")

print("\nKeys containing GST numbers:")
for key, value in identify_key(data, gst_pattern):
    validity = 'valid' if gst_pattern.match(value) else 'invalid'
    print(f"{key}: {value} is {validity}")
"""


import json
import re

def identify_key(data, pattern):
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
                elif isinstance(v, str) and pattern.match(v):
                    identified_keys.append((nested_key, v))

    return identified_keys

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Identify keys containing Aadhar, PAN, and GST numbers and directly print the output
aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')

print("Keys containing Aadhar numbers:")
for key, value in identify_key(data, aadhar_pattern):
    validity = 'valid' if aadhar_pattern.match(value) else 'invalid'
    print(f"{key}: {value} is {validity}")

print("\nKeys containing PAN numbers:")
for key, value in identify_key(data, pan_pattern):
    validity = 'valid' if pan_pattern.match(value) else 'invalid'
    print(f"{key}: {value} is {validity}")

print("\nKeys containing GST numbers:")
for key, value in identify_key(data, gst_pattern):
    validity = 'valid' if gst_pattern.match(value) else 'invalid'
    print(f"{key}: {value} is {validity}")
