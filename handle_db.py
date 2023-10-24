import boto3
from faker import Faker

REGION = 'us-east-1'
TABLE = 'phonedb'

def create_dynamodb_table_if_not_exists():
    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table_name = TABLE

    existing_tables = dynamodb.meta.client.list_tables()
    
    if table_name not in existing_tables['TableNames']:
        table = dynamodb.create_table(
            TableName=TABLE,
            KeySchema=[
                {
                    'AttributeName': 'PhoneNumber',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PhoneNumber',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()

def populate_dynamodb_table():
    dynamodb = boto3.client('dynamodb', region_name=REGION)
    table_name = TABLE

    fake = Faker()
    phone_numbers = [fake.phone_number() for _ in range(100)]

    for phone_number in phone_numbers:
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'PhoneNumber': {'S': phone_number}
            }
        )

if __name__ == '__main__':
    create_dynamodb_table_if_not_exists()
    populate_dynamodb_table()
