import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    try:
        table = dynamodb.Table('LeaveRequestsTable')
        table.update_item(
            Key={'EmployeeId': event['EmployeeId']},
            UpdateExpression='SET #Status = :s',
            ExpressionAttributeNames={'#Status': 'Status'},
            ExpressionAttributeValues={':s': event['status']}
        )

        return {'statusCode': 200, 'body': 'Leave request status updated successfully.'}

    except ClientError as e:
        print('Error:', e)
        return {'statusCode': 500, 'body': f'{{"error": "{e.response["Error"]["Message"]}"}}'}

    except Exception as e:
        print('Error:', e)
        return {'statusCode': 500, 'body': f'{{"error": "{str(e)}"}}'}
