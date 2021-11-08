import boto3
import json
import os
import typing

client = boto3.client('lambda')
account_id = os.environ['ACCOUNT_ID']
region = os.environ['REGION']


def invokeLambdaFunction(*, functionName: str = None, payload: typing.Mapping[str, str] = None):
    if functionName == None:
        raise Exception('ERROR: functionName parameter cannot be NULL')
    # payloadStr = json.dumps(payload)
    # payloadBytesArr = bytes(payloadStr, encoding='utf8')
    response = client.invoke(
        FunctionName=functionName,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )
    return response


def lambda_handler(event, context):
    payloadObj = {"something": "Bad News!"}
    response = invokeLambdaFunction(
        functionName=f'arn:aws:lambda:{region}:{account_id}:function:demo-python', payload=payloadObj)
    print(f'response:{response}')
    return f'response:{response}'
