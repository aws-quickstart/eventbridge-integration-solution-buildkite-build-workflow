import json
import os
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ['s3_bucket_name']
    build_name = event['detail']['build']['message']
    build_number = event['detail']['build']['number']
    key = build_name+str(build_number)+'/event_payload.json'
    s3_client.put_object(Body=json.dumps(event), Bucket=bucket_name, Key=key)

    result = {
        'build_name': build_name,
        'build_number': build_number,
        'build_state': event['detail']['build']['state'],
        'pipeline': event['detail']['pipeline']['slug'],
    }

    return result
    