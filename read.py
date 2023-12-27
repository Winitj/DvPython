

"""
import json
import re

def validate_aadhar(aadhar):
    pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
    return bool(pattern.match(aadhar))

def validate_pan(pan):
    pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
    return bool(pattern.match(pan))

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Iterate over each person and validate Aadhar and PAN
for person in data['persons']:
    name = person['name']
    aadhar_number = person['aadhar']
    pan_number = person['pan']

    print(f"\nValidating details for {name}:")
    
    # Validate Aadhar
    if validate_aadhar(aadhar_number):
        print("Aadhar number is valid")
    else:
        print("Aadhar number is not valid")

    # Validate PAN
    if validate_pan(pan_number):
        print("PAN number is valid")
    else:
        print("PAN number is not valid")
      """ 
import json
import re

def identify_key(data, key_type, pattern):
    identified_keys = []

    def recursive_search(obj, current_key=''):
        if isinstance(obj, list):
            for i, item in enumerate(obj):
                recursive_search(item, current_key=f'{current_key}[{i}]')
        elif isinstance(obj, dict):
            for k, v in obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    recursive_search(v, current_key=nested_key)
                elif isinstance(v, str) and pattern.match(v):
                    identified_keys.append((nested_key, v))

    recursive_search(data)
    return identified_keys

def validate_aadhar(aadhar):
    pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$') 
    return bool(pattern.match(aadhar))

def validate_pan(pan):
    pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
    return bool(pattern.match(pan))

def validate_gst(gst):
    pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')
    return bool(pattern.match(gst))

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Identify keys containing Aadhar, PAN, and GST numbers
aadhar_keys = identify_key(data, 'Aadhar', re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$'))
pan_keys = identify_key(data, 'PAN', re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$'))
gst_keys = identify_key(data, 'GST', re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$'))

# Display the identified keys
print("Keys containing Aadhar numbers:")
for key, value in aadhar_keys:
    print(f"{key}: {value} is valid")

print("\nKeys containing PAN numbers:")
for key, value in pan_keys:
    print(f"{key}: {value} is valid")

print("\nKeys containing GST numbers:")
for key, value in gst_keys:
    print(f"{key}: {value} is valid") 

#20440 function calls (19019 primitive calls) in 0.100 seconds   test2
#9968 function calls (9453 primitive calls) in 0.059 seconds     test1

"""
import json
import re

def identify_key(data, key_type, pattern):
    identified_keys = []

    def recursive_search(obj):
        if isinstance(obj, list):
            for item in obj:
                recursive_search(item)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    recursive_search(v)
                elif isinstance(v, str) and pattern.match(v):
                    identified_keys.append((k, v))

    recursive_search(data)
    return identified_keys

def validate_aadhar(aadhar):
    pattern = re.compile(r'^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$')
    return bool(pattern.match(aadhar))

def validate_pan(pan):
    pattern = re.compile(r'^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$')
    return bool(pattern.match(pan))

def validate_gst(gst):
    pattern = re.compile(r'^([0-3]{1}[0-9]{1}|[9]{1}[8-9]{1})[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}([1-9]|[A-Z]){1}$')
    return bool(pattern.match(gst))

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Identify keys containing Aadhar, PAN, and GST numbers
aadhar_keys = identify_key(data, 'Aadhar', re.compile(r'^[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}$'))
pan_keys = identify_key(data, 'PAN', re.compile(r'^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$'))
gst_keys = identify_key(data, 'GST', re.compile(r'^([0-3]{1}[0-9]{1}|[9]{1}[8-9]{1})[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}([1-9]|[A-Z]){1}$'))

# Display the identified keys
print("Keys containing Aadhar numbers:")
for key, value in aadhar_keys:
    print(f"{key}: {value}")

print("\nKeys containing PAN numbers:")
for key, value in pan_keys:
    print(f"{key}: {value}")

print("\nKeys containing GST numbers:")
for key, value in gst_keys:
    print(f"{key}: {value}")
"""
"""

import json
import re

aadhar_pattern = re.compile(r'^[2-9]\d{3}\s\d{4}\s\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{3}[PCHABGJLFT]{1}[A-Z]{1}(?!0000)\d{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^([0-3]\d|[9][8-9])[A-Z]{3}[PCHABGJLFT]{1}[A-Z](?!0000)\d{4}[A-Z]\d{1}Z([1-9A-Z]){1}$')


def identify_keys(data, pattern):
    identified_keys = []

    def recursive_search(obj):
        if isinstance(obj, list):
            for item in obj:
                recursive_search(item)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    recursive_search(v)
                elif isinstance(v, str) and pattern.match(v):
                    identified_keys.append((k, v))

    recursive_search(data)
    return identified_keys

def validate_number(number, pattern):
    return bool(pattern.match(number))

json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)



aadhar_keys = identify_keys(data, aadhar_pattern)
pan_keys = identify_keys(data, pan_pattern)
gst_keys = identify_keys(data, gst_pattern)

print("Keys containing Aadhar numbers:")
for key, value in aadhar_keys:
    print(f"{key}: {value}")

print("\nKeys containing PAN numbers:")
for key, value in pan_keys:
    print(f"{key}: {value}")

print("\nKeys containing GST numbers:")
for key, value in gst_keys:
    print(f"{key}: {value}")
 """
