import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference to the DynamoDB table
table = dynamodb.Table('RegistrationTable')

def lambda_handler(event, context):
    try:
        # API Gateway sends the payload directly, so we don't need to parse 'body'
        id = event['id']
        name = event['name']
        department = event['department']

        # Construct the item to be inserted into DynamoDB
        item = {
            'id': id,
            'name': name,
            'department': department
        }

        # Store the item in the DynamoDB table
        table.put_item(Item=item)

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Student registration successful',
                'data': item
            })
        }

    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Missing required field: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }