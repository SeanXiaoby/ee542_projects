# example for reading and writing to DB

import json
import base64
import boto3
from decimal import Decimal
import requests

client = boto3.client('dynamodb')
table = boto3.resource('dynamodb').Table('final')


def read():
    response = client.get_item(
        TableName='final',
        Key={
            'xdotId': {
                'N': "0"
            }
        }
    )

    response = client.scan(
        TableName='final',
    )
    print(response)


def write():
    data = client.put_item(
        TableName='final',
        Item={
            'xdotId': {
                'N': 1
            },
            'sensor': {
                'S': 'wyxwyxwyx'
            }
        }
    )


def to_decimal(num):
    item = json.loads(json.dumps(num), parse_float=Decimal)
    return item


def update():
    reading = {'xdotId': '4', 'lat': '31.02755934255644', 'lng': '-118.29494717425943', 'moved': False}

    # response = table.update_item(
    #     Key={
    #         'xdotId': 1,
    #     },
    #     UpdateExpression="set lat = :r",
    #     ExpressionAttributeValues={
    #         ':r': to_decimal(34.033797921083035),
    #     },
    #     ReturnValues="UPDATED_NEW"
    # )

    response = table.update_item(
        Key={
            'xdotId': int(reading['xdotId']),
        },
        UpdateExpression="set lat = :r, lng = :m, moved = :n",
        ExpressionAttributeValues={
            ':r': to_decimal(float(reading['lat'])),
            ':m': to_decimal(float(reading['lng'])),
            ':n': reading['moved']
        },
        ReturnValues="UPDATED_NEW"
    )

    print(response)


if __name__ == "__main__":
    update()
