import os

import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')

def startSetup(whichTable: str):
    """Start the setup of the dynamoDB
    Args:
        whichTable (str): table from dynamoDB
    Returns:
        _type_: _description_
    """
    resource = boto3.resource(
        'dynamodb',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = REGION_NAME
    )
    table = resource.Table(whichTable)
    return table