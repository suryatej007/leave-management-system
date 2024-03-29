import json
import boto3

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    try:
        # Extract EmployeeId from the event
        employee_id = event['EmployeeId']
        status=event['status']
        
        # Construct email address by appending "@gmail.com"
        employee_email = f"{employee_id}cseh@gmail.com"
        
        # Construct email message
        subject = 'Leave Request Status Update'
        message = f"Status update for Employee ID: {employee_id}\n\nYour leave have been {status} "
        
        # Send email to employee
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [employee_email]
            },
            Message={
                'Body': {
                    'Text': {
                        'Data': message
                    }
                },
                'Subject': {
                    'Data': subject
                }
            },
            Source='suryatejadasari16@gmail.com'  # Replace with your verified SES email address
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully'})
        }
    except Exception as e:
        print(f"Error sending email: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
