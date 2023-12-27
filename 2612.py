
"""
# importing required module
import urllib.parse
import requests

# setting the base URL value
baseUrl = "https://v6.exchangerate-api.com/v6/0f215802f0c83392e64ee40d/pair/"

First = input("Enter First Currency Value\n")
Second = input("Enter Second Currency Value\n")

result = First+"/"+Second
final_url = baseUrl+result

# retrieving data from JSON Data
json_data = requests.get(final_url).json()
Final_result = json_data['conversion_rate']

print("Conversion rate from "+First+" to "+Second+" = ", Final_result)


"""  """ # Open the JSON file for reading
import json
with open('C:/Users/jain vinit/Documents/Python/test2.json', 'r') as file:
    # Parse JSON data
    data = json.load(file)

# Display the data
print(data)

"""

import json

json_string = '{"name": "Boston", "state": "MA", "population": 685094}'

# Parse JSON data from a string
city = json.loads(json_string)

# Display the data
print(city)

city = data['city']

# Loop through the array and print each city name
for city in cities:
    print(city['name'])


