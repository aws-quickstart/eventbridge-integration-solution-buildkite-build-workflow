import json
from datetime import datetime

def lambda_handler(event, context):
    name = event['build_name']
    number = event['build_number']
    state = event['build_state']
    pipeline_name=event['pipeline']
    
    subject = "Build result for "+name+" #"+str(number)
    message = "Hello, your build, "+name+" #"+str(number)+", from "+pipeline_name+" pipeline, has "+state+"."

    return {"message": message, "subject":subject}