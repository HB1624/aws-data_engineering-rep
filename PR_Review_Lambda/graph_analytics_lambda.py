import json
import os

def handler(event, context):
    env = os.environ.get("ENVIRONMENT", "dev")
    print(f"Received event: {json.dumps(event)}")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hello from Lambda running in '{env}'!"})
