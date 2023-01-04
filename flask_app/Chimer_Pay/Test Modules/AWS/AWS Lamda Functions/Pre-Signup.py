import json

def lambda_handler(event, context):
    # # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    
    event["response"]["autoConfirmUser"]=True
    event["response"]["autoVerifyPhone"]=True
    
    
    # print(json.dumps(event))
    
    return event