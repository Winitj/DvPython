"""
import json
import os


json_file_path = 'C:\\Users\\jain vinit\\Documents\\Python\\Updated-Job-Run 1.json'

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        file_content = json_file.read()
        print(file_content)
        json_data = json.loads(file_content)
    print(json_data)
else:
    print(f"Error: File not found at {json_file_path}")

"""
"""

import json
import os
from datetime import datetime

# Load data from the job_run.json file
json_file_path = 'C:\\Users\\jain vinit\\Documents\\Python\\Updated-Job-Run 1.json'  # Replace with the actual path to your file
"""   """
if not json_file_path:
    print("Error: Please provide the correct path to the job_run.json file.")
    exit()

with open(json_file_path, 'r') as json_file:
    job_data = json.load(json_file)

# Extract relevant information for the first JSON file
job_info = {
    "JobID": job_data["Id"],
    "JobName": job_data["JobName"],
    "StartTime": str(job_data["StartedOn"]),
    "EndTime": str(job_data["CompletedOn"]),
    "WorkerType": job_data["WorkerType"],
    "JobStatus": job_data["JobRunState"],
    "ExecutionTime": job_data["ExecutionTime"],
    "NumberOfWorkers": job_data["NumberOfWorkers"]
}

# Save the first JSON file
output_file_path_1 = 'C:\\Users\\jain vinit\\Documents\\Python\\output.json'  # Replace with the desired output path
with open(output_file_path_1, 'w') as output_file_1:
    json.dump(job_info, output_file_1, indent=2)

# Extract relevant information for the second JSON file (Job Summary)
job_summary = {
    "TotalRuns": 1,  # Assuming you have data for a single job run
    "SuccessfulJobs": 1 if job_data["JobRunState"] == "SUCCEEDED" else 0,
    "StoppedJobs": 1 if job_data["JobRunState"] == "STOPPED" else 0,
    "RunningJobs": 1 if job_data["JobRunState"] == "RUNNING" else 0
}

# Save the second JSON file
output_file_path_2 = 'C:\\Users\\jain vinit\\Documents\\Python\\sum.json'  # Replace with the desired output path
with open(output_file_path_2, 'w') as output_file_2:
    json.dump(job_summary, output_file_2, indent=2)

print(f"Data extracted and saved to {output_file_path_1} and {output_file_path_2}.")
"""
"""
import json
from datetime import datetime

# Replace 'path/to/job_run.json' with the actual path to your file
json_file_path = 'C:\\Users\\jain vinit\\Documents\\Python\\Updated-Job-Run 1.json'

if not json_file_path:
    print("Error: Please provide the correct path to the job_run.json file.")
    exit()

# Read the content of the JSON file
with open(json_file_path, 'r') as json_file:
    try:
        job_data = json.load(json_file)
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit()

# Extract relevant information for the first JSON file
job_info = {
    "JobID": job_data.get("Id", ""),
    "JobName": job_data.get("JobName", ""),
    "StartTime": str(job_data.get("StartedOn", "")),
    "EndTime": str(job_data.get("CompletedOn", "")),
    "WorkerType": job_data.get("WorkerType", ""),
    "JobStatus": job_data.get("JobRunState", ""),
    "ExecutionTime": job_data.get("ExecutionTime", ""),
    "NumberOfWorkers": job_data.get("NumberOfWorkers", "")
}

# Save the first JSON file
output_file_path_1 = 'C:\\Users\\jain vinit\\Documents\\Python\\sum.json'
with open(output_file_path_1, 'w') as output_file_1:
    json.dump(job_info, output_file_1, indent=2)

# Extract relevant information for the second JSON file (Job Summary)
job_summary = {
    "TotalRuns": 1,  # Assuming you have data for a single job run
    "SuccessfulJobs": 1 if job_data.get("JobRunState", "") == "SUCCEEDED" else 0,
    "StoppedJobs": 1 if job_data.get("JobRunState", "") == "STOPPED" else 0,
    "RunningJobs": 1 if job_data.get("JobRunState", "") == "RUNNING" else 0
}

# Save the second JSON file
output_file_path_2 = 'C:\\Users\\jain vinit\\Documents\\Python\\output.json'
with open(output_file_path_2, 'w') as output_file_2:
    json.dump(job_summary, output_file_2, indent=2)

print(f"Data extracted and saved to {output_file_path_1} and {output_file_path_2}.")

"""

import json
from datetime import datetime
from dateutil.tz import tzlocal

job_data = [
{
    "Id": "jr_fe96fa",
    "Attempt": 0,
    "JobName": "as-final-stepfunction-gluejob",
    "StartedOn": datetime(2023, 12, 12, 15, 54, 50, 146000, tzinfo=tzlocal()),
    "LastModifiedOn": datetime(2023, 12, 12, 15, 55, 30, 406000, tzinfo=tzlocal()),
    "CompletedOn": datetime(2023, 12, 12, 15, 55, 30, 406000, tzinfo=tzlocal()),
    "JobRunState": "SUCCEEDED",
    "PredecessorRuns": [],
    "AllocatedCapacity": 10,
    "ExecutionTime": 32,
    "Timeout": 2880,
    "MaxCapacity": 10.0,
    "WorkerType": "G.1X",
    "NumberOfWorkers": 10,
    "LogGroupName": "/aws-glue/jobs",
    "GlueVersion": "4.0",
    "ExecutionClass": "STANDARD"
},
{
    "Id": "6fa",
    "Attempt": 0,
    "JobName": "as-final-stepfunction-gluejob",
    "StartedOn": datetime(2023, 12, 12, 15, 54, 50, 146000, tzinfo=tzlocal()),
    "LastModifiedOn": datetime(2023, 12, 12, 15, 55, 30, 406000, tzinfo=tzlocal()),
    "CompletedOn": datetime(2023, 12, 12, 15, 55, 30, 406000, tzinfo=tzlocal()),
    "JobRunState": "SUCCEEDED",
    "PredecessorRuns": [],
    "AllocatedCapacity": 10,
    "ExecutionTime": 32,
    "Timeout": 2880,
    "MaxCapacity": 10.0,
    "WorkerType": "G.1X",
    "NumberOfWorkers": 10,
    "LogGroupName": "/aws-glue/jobs",
    "GlueVersion": "4.0",
    "ExecutionClass": "STANDARD"
},
{
    "Id": "a",
    "Attempt": 0,
    "JobName": "as-final-stepfunction-gluejob",
    "StartedOn": datetime(2023, 12, 12, 15, 54, 50, 146000, tzinfo=tzlocal()),
    "LastModifiedOn": datetime(2023, 12, 12, 15, 55, 30, 406000, tzinfo=tzlocal()),
    "CompletedOn": datetime(2023, 12, 12, 15, 55, 30, 406000, tzinfo=tzlocal()),
    "JobRunState": "SUCCEEDED",
    "PredecessorRuns": [],
    "AllocatedCapacity": 10,
    "ExecutionTime": 32,
    "Timeout": 2880,
    "MaxCapacity": 10.0,
    "WorkerType": "G.1X",
    "NumberOfWorkers": 10,
    "LogGroupName": "/aws-glue/jobs",
    "GlueVersion": "4.0",
    "ExecutionClass": "STANDARD"
}
  
   
]

for idx, job_data in enumerat
(job_data, start=1):
    
    job_details = {
        "Job ID": job_data.get("Id", ""),
        "Job Name": job_data.get("JobName", ""),
        "Start Time": job_data.get("StartedOn", "").isoformat(),
        "End Time": job_data.get("CompletedOn", "").isoformat(),
        "Worker type": job_data.get("WorkerType", ""),
        "Job Status": job_data.get("JobRunState", ""),
        "Execution Time": job_data.get("ExecutionTime", ""),
        "Number Of Workers": job_data.get("NumberOfWorkers", "")
    }

   
    job_summary = {
        "Total Runs": 1,  # Assuming this is a single job run
        "Successful Job": 1 if job_data.get("JobRunState") == "SUCCEEDED" else 0,
        "Stopped Job": 1 if job_data.get("JobRunState") == "STOPPED" else 0,
        "Running Job": 1 if job_data.get("JobRunState") == "RUNNING" else 0
    }



with open('C:\\Users\\jain vinit\\Documents\\Python\\output.json', 'w') as json_output_file:
    json.dump(job_details, json_output_file, indent=2)

with open('C:\\Users\\jain vinit\\Documents\\Python\\sum.json', 'w') as json_output_file:
    json.dump(job_summary, json_output_file, indent=2)


