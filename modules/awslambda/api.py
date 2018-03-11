# Ben Humphrey
# github.com/complexitydev
# ben@complexitydevelopment.com


import json

import boto3


def process(service, request):
    # api = "https://r7trx4otp0.execute-api.us-east-2." \
    #       "amazonaws.com/discordFetch/service={}&request={}".format(service, request)
    # print("made it here")
    # req = urllib.request.Request(
    #     api,
    #     data=None,
    #     headers={
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 '
    #                       '(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    #         'site': service,
    #         'lookup': request
    #     }
    # )
    # urllib.request.urlopen(req)
    test = {}
    test['site'] = "dotabuff"
    test['request'] = "mid"
    client = boto3.client('lambda', region_name='us-east-2')
    response = client.invoke(
        FunctionName='arn:aws:lambda:us-east-2:332807454899:function:lambda-html',
        InvocationType='RequestResponse',
        LogType='None',
        Payload=json.dumps(test)
    )
    data = response['Payload'].read()
    print(data)

process("dotabuff", "mid")
