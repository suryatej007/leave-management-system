import json
import boto3

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    try:
        # Extract data from the event
        employee_id = event['EmployeeId']
        applicant_email = event['ApplicantEmail']
        leave_dates = event['LeaveDates']
        
        # Adjust leave_dates format if needed
        leave_dates = leave_dates.replace('/', '-')
        
        subject = 'Leave Request Submitted'
        message = f"Leave request submitted:\n\nEmployee ID: {employee_id}\nApplicant Email: {applicant_email}\nLeave Dates: {leave_dates}"
        
        # Send email to HR
        response = ses_client.send_email(
            Destination={
                'ToAddresses': ['suryatejadasari16@gmail.com']  # Replace with the HR's email address
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
            'body': json.dumps({'message': 'Email sent to HR successfully'})
        }
    except Exception as e:
        print(f"Error sending email to HR: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
