import json

def lambda_handler(event, context):
    # TODO implement

    
    print(json.dumps(event))
    
    event['response']['privateChallengeParameters']                 = dict()

    # this is the OTP replace opensesame with OTP
    # Use SNS service and store the OPT here
    event['response']['privateChallengeParameters']['challenge']    = "opensesame"


    
    return event