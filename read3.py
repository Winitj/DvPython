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

def validate_and_print(keys, pattern, label):
    print(f"Keys containing {label} numbers:")
    for key, value in keys:
        validity = 'valid' if pattern.match(value) else 'invalid'
        print(f"{key}: {value} is {validity}")

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Identify keys containing Aadhar, PAN, and GST numbers
aadhar_keys = identify_key(data, re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$'))
pan_keys = identify_key(data, re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$'))
gst_keys = identify_key(data, re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$'))

# Display the identified keys and their validity
validate_and_print(aadhar_keys, re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$'), 'Aadhar')
validate_and_print(pan_keys, re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$'), 'PAN')
validate_and_print(gst_keys, re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$'), 'GST')

