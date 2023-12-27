import time
import datetime
import json
from dateutil.tz import tzlocal
import re
import dateutil.parser

json_data = [
    {
        "Id": "jr_fe96fa36b6aad130610568eb874377eda5ca913f031c2cc0e17dff6212a3843d",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,12,15,54,50,146000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,12,15,55,30,406000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,12,15,55,30,406000, tzinfo=tzlocal()),
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
        "Id": "jr_d75d6bd88caabfe39c71c83df86a1ccadfeff0e0f2d2e218443db8df24591e3e",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,12,15,54,45,597000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,12,15,55,37,521000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,12,15,55,37,521000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 45,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_b71227c583dac752bdc2a0a20eee2d3de3a435a4bf9925ca2127cf185d5959df",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,12,15,54,41,755000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,12,15,55,22,317000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,12,15,55,22,317000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 34,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_f0b668b3595fd29578f11595dd5dddf24f965a0f8dd8b7f4a1b50146470ac7ed",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,12,15,54,37,755000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,12,15,55,16,369000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,12,15,55,16,369000, tzinfo=tzlocal()),
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
        "Id": "jr_4e31bed21ceed21de4cf54341fe0e829173fe384f9b6949311ea4d015354d6b2",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,12,15,54,34,128000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,12,15,55,20,277000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,12,15,55,20,277000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 39,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_103178de102f168c702d15e73c89f3cd607237ca213f76f0f4d4e5e64a603342",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023, 12, 12, 15, 54, 28, 890000, tzinfo=tzlocal()), 
        "LastModifiedOn": datetime.datetime(2023, 12, 12, 15, 55, 13, 789000, tzinfo=tzlocal()), 
        "CompletedOn": datetime.datetime(2023, 12, 12, 15, 55, 13, 789000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 38,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_18ff42569910dacdca8184cb9613b0e5171740f501c9676998d8ed3947fcbfab",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,12,15,54,13,940000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,12,15,55,7,836000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,12,15,55,7,836000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 47,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_3cffea3de2df3aa26786ad6988b58565f29d6da41b33fb3e91284a115b1c6095",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,28,46,466000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,29,28,508000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,29,28,508000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 34,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_30cdcb64eb868c43884299c4383e95a8f3f07e94c44b99765844795490dc09ea",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,28,39,882000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,29,35,930000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,29,35,930000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 45,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_da6229bcc14e71aa600444f7616efcc3c095c697370a2f20b3ddfd1232617564",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,28,34,166000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,29,16,166000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,29,16,166000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_1e1081101f7b3323cfbe6c1786fb58a3b196cb62d8977a024419d22325db72d1",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,28,28,315000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,29,11,121000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,29,11,121000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 36,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_1e3bded4adc6a5d66271d1d6fd50d7f89e7b703277aa8f4436349a7130cdb3af",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,28,22,145000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,29,4,582000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,29,4,582000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 36,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_aba65302288d3a1c0e121f62fd787b148c2385605b426fa78b618692e6a6c4ef",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,28,15,444000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,29,9,410000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,29,9,410000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 47,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_314e212286833a6a2d9b48374392770b52bf89bd2e1d0147d97450fea02fe57e",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,16,15,6,889000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,15,58,728000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,15,58,728000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 44,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_63b4d0803b3d113333ac7f6e2496bc49e315ba6cf53d5236805060ba68cb88b8",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,15,59,53,578000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,16,0,35,126000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,16,0,35,126000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_c40aff630f982f450550911ff340053d78446288ad3d3ed6f5cd489147efcb0e",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,15,49,53,81000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,15,50,28,15000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,15,50,28,15000, tzinfo=tzlocal()),
        "JobRunState": "FAILED",
        "ErrorMessage": "GlueArgumentError: the following arguments are required: --s3_bucket",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 28,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_d3178b84256f734dfefb6f56ee86dbe2e0110f6364fc671fb4f62c0dbbcffbc2",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,12,11,15,48,2,312000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,12,11,15,48,52,754000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,12,11,15,48,52,754000, tzinfo=tzlocal()),
        "JobRunState": "FAILED",
        "ErrorMessage": "GlueArgumentError: the following arguments are required: --s3_bucket",
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 43,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_b3cf0fbb186db21a62f89d5479107fd86a965a246f00afa8a987fd1e69472573",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,7,26,14,7,49,36000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,7,26,14,8,32,481000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,7,26,14,8,32,481000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3: //sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=04/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 36,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_e67e4878cda3e8fa3ac4f1fa63ec68601c63785f672d395c4c89d39bdfaae762",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,7,26,14,7,49,9000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,7,26,14,8,32,676000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,7,26,14,8,32,676000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=05/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 36,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_7bcd2f9ae0dca9bf5ed8d7f1bcbbe172c44b28741dcb54f75efad85017e2e875",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        18,
        33,
        10,
        421000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        18,
        46,
        50,
        613000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        18,
        46,
        50,
        613000, tzinfo=tzlocal()),
        "JobRunState": "STOPPED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=16/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 812,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_4f4a997618e2df9bd1b89629d787411e5152f24a15ab55dc4b63a504baf75b81",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        15,
        8,
        9,
        327000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        15,
        22,
        23,
        255000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        15,
        22,
        23,
        255000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=16/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 846,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_b0d36fad9f225a016382129eeec9667f831f74efc1919701e51ae4c57862e132",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        15,
        8,
        9,
        267000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        15,
        8,
        54,
        126000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        15,
        8,
        54,
        126000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=15/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 37,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_a3588d63c6bb0e6e5cbf43f6cd2a673bb3255c27e71b6ecd8e410f85d3e9c6f1",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        12,
        29,
        18,
        43000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        12,
        29,
        58,
        680000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        12,
        29,
        58,
        680000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=04/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 34,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_c25d789992f6b179fc3b5ca2811f0de3e13e6b52dfb9168fed1bd1c9459443a2",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        12,
        29,
        18,
        9000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        12,
        30,
        1,
        65000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        12,
        30,
        1,
        65000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=03/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 36,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_af1422e94361475aba2b256dbb7d2993089f7eb7ae10847384d8901ffe146250",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        716000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        12,
        1,
        35,
        59000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        12,
        1,
        35,
        59000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=01/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 764,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_64f6d80f7639645673bb7c4c5c93a2590d8e100a4dd28d52cf3aa6c7c92dc9b9",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        601000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        31,
        100000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        31,
        100000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=03/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 37,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_bc60911e391759a8880830cc188ee4d80d36581816dece1e330a05775afa4a66",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        575000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        12,
        1,
        44,
        426000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        12,
        1,
        44,
        426000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=02/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 774,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_fb1a2b83383fbf1ddc89ded577131e7497a992714ba5bd977dfa0e84b2e661b3",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        566000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        31,
        701000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        31,
        701000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=08/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_45dcdedd2e5cbc23e7609e25acce3fd9ea63a8bc2d210e358a12d315ff148f50",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        563000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        27,
        794000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        27,
        794000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=07/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_a76bc27f31a7c1f371b6f3735cbbf15d48295adacd59fe2d358a378bfa5c3748",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        562000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        29,
        149000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        29,
        149000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=06/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_a2fb255c14da39b3c317223e42055de3fdd84bad9024516a2396cf1eda9bcf2b",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        559000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        28,
        226000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        28,
        226000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=15/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 33,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_84a03951da7f7ed10ee95f93d2575e0dad6242190ee1ba2ccfc329a0c70814db",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        558000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        26,
        552000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        26,
        552000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=05/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_a667f8d44fba6ee3b5eeb4afacd8ed0e6f4ddc16c8936fe7a6763e6e9c34cb79",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        557000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        29,
        81000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        29,
        81000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=12/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_a88e5a5f2f9f8f8a3791907c6501277c5c461a41b9a0f2b33a5ff0606034fd31",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        549000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        31,
        843000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        31,
        843000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=09/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 34,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_9f606b1d11eb2f3f396e016788e3b8bafa980607b0c4534e1645c06a037c00f8",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        545000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        25,
        69000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        25,
        69000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=10/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_c795c3934749ce8c9b2e9d117007db9048f96b726192c6860371a45bbcdcbe39",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        543000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        26,
        810000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        26,
        810000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=14/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 33,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_fafeaed04914910013a79a13c21d0de5d74dec42356dd513564da65b527a6853",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        540000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        25,
        749000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        25,
        749000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=13/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 34,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_4ca2ab325ec48bb4b940e7851a52ab477cb1fdb14c694e75244966cb6a942469",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        535000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        28,
        452000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        28,
        452000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=11/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 38,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    },
    {
        "Id": "jr_4278499535195406d4b21d0aeb3da7d29211844df1bde8ecfe5c3d0366b860b9",
        "Attempt": 0,
        "JobName": "as-final-stepfunction-gluejob",
        "StartedOn": datetime.datetime(2023,
        7,
        24,
        11,
        48,
        43,
        523000, tzinfo=tzlocal()),
        "LastModifiedOn": datetime.datetime(2023,
        7,
        24,
        11,
        49,
        25,
        498000, tzinfo=tzlocal()),
        "CompletedOn": datetime.datetime(2023,7,24,11,49,25,498000, tzinfo=tzlocal()),
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--s3_bucket": "s3://sociomatrix-testdata-nonprod-185492734037/Prod-structure/year=2023/month=06/day=04/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 35,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "4.0",
        "ExecutionClass": "STANDARD"
    }]
    
json1 = []
json2 = []

json1_params = ['Id',"JobName","WorkerType","JobRunState","ExecutionTime","NumberOfWorkers"]
date_params = ["StartedOn","CompletedOn"]

for obj in json_data:
    new_obj1 = {}
    new_obj2 = {}
    for key in obj.keys():
        if key in date_params:
            new_obj1[str(key)] = str(obj[key].isoformat())
        elif key == "LastModifiedOn":
            new_obj2[key] = str(obj[key].isoformat())
        elif key in json1_params:
            new_obj1[key] = obj[key]
        else:
            new_obj2[key] = obj[key]
    json1.append(new_obj1)
    json2.append(new_obj2)

# print(json1)

with open('json1.json','w') as json1_file, open('json2.json','w') as json2_file :
    json.dump(json1,json1_file,indent=4)
    json.dump(json2,json2_file,indent=4)

