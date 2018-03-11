# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com


import json

import boto3


def process(service, request):
    test = {'site': service, 'lookup': request}
    client = boto3.client('lambda', region_name='us-east-2')
    response = client.invoke(
        FunctionName='arn:aws:lambda:us-east-2:332807454899:function:lambda-html',
        InvocationType='RequestResponse',
        LogType='None',
        Payload=json.dumps(test)
    )
    data = response['Payload'].read().decode()
    return data
