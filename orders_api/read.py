import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    #order = {'id': 123, 'itemName': 'Mac', 'quantity': 100}
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('ORDERS_TABLE')
    table = dynamodb.Table(table_name)
    order_id = int(event['pathParameters']['vehicle_id'])
    response = table.query(KeyConditionExpression=Key('vehicle_id').eq(order_id))
    return{
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }


