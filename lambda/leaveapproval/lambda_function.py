import json
from boto3.dynamodb.conditions import Attr
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LeaveRequestsTable')

    response = table.scan(
        FilterExpression=Attr('Status').exists() & Attr('Status').eq('Pending')
    )

    leave_requests = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(leave_requests)
    }
