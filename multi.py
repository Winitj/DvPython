import json
import re
from multiprocessing import Pool

def identify_and_validate_keys(item):
    keys, patterns = item
    identified_keys = []

    for key, value in keys:
        for pattern_type, pattern in patterns.items():
            if pattern.match(value):
                validity = 'valid' if validate_number(value, pattern) else 'invalid'
                identified_keys.append((key, value, pattern_type, validity))

    return identified_keys

def validate_number(number, pattern):
    return bool(pattern.match(number))

def chunk_data(data, chunk_size):
    """Divide the data into chunks for parallel processing."""
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Specify the path to your JSON file
json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

# Open the file in read mode
with open(json_file_path, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Compile patterns outside the loop
aadhar_pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
pan_pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
gst_pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')

patterns = {'Aadhar': aadhar_pattern, 'PAN': pan_pattern, 'GST': gst_pattern}

# Identify keys containing Aadhar, PAN, and GST numbers
aadhar_keys = identify_and_validate_keys(data, 'Aadhar', aadhar_pattern)
pan_keys =  identify_and_validate_keys(data, 'PAN', pan_pattern)
gst_keys =  identify_and_validate_keys(data, 'GST', gst_pattern)

# Combine all keys for parallel processing
all_keys = aadhar_keys + pan_keys + gst_keys

# Split the data into chunks for parallel processing
chunk_size = len(all_keys) // 4  # Adjust the number of chunks based on your system's capabilities
data_chunks = chunk_data(all_keys, chunk_size)

# Use multiprocessing to parallelize the identification and validation tasks
with Pool() as pool:
    results = pool.map(identify_and_validate_keys, [(chunk, patterns) for chunk in data_chunks])

# Flatten the results
identified_keys = [item for sublist in results for item in sublist]

# Display the identified and validated keys
for key, value, pattern_type, validity in identified_keys:
    print(f"{key}: {value} is {validity} for {pattern_type}")
