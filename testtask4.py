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

for idx, job_data in enumerate(job_data, start=1):
    
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



all_job_summary = {
    "Total Runs": 0,
    "Successful Job": 0,
    "Stopped Job": 0,
    "Running Job": 0
}

all_job_details = []

for idx, job_data_entry in enumerate(job_data, start=1):
  
    job_details = [{
        "Job ID": job_data_entry.get("Id", ""),
        "Job Name": job_data_entry.get("JobName", ""),
        "Start Time": job_data_entry.get("StartedOn", "").isoformat(),
        "End Time": job_data_entry.get("CompletedOn", "").isoformat(),
        "Worker type": job_data_entry.get("WorkerType", ""),
        "Job Status": job_data_entry.get("JobRunState", ""),
        "Execution Time": job_data_entry.get("ExecutionTime", ""),
        "Number Of Workers": job_data_entry.get("NumberOfWorkers", "")
    }
    ]
    
    all_job_details.append(job_details)

   
    all_job_summary["Total Runs"] += 1
    if job_data_entry.get("JobRunState") == "SUCCEEDED":
        all_job_summary["Successful Job"] += 1
    elif job_data_entry.get("JobRunState") == "STOPPED":
        all_job_summary["Stopped Job"] += 1
    elif job_data_entry.get("JobRunState") == "RUNNING":
        all_job_summary["Running Job"] += 1


with open('C:\\Users\\jain vinit\\Documents\\Python\\output.json', 'w') as json_output_file:
    json.dump(all_job_details, json_output_file, indent=2)

with open('C:\\Users\\jain vinit\\Documents\\Python\\sum.json', 'w') as json_output_file:
    json.dump(all_job_summary, json_output_file, indent=2)
