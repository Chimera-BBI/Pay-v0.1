import json

def lambda_handler(event, context):
    # TODO implement
    
    print(json.dumps(event))
    
    event['response']['challengeName'] = "CUSTOM_CHALLENGE"
        
    if(event['request']['userNotFound']):
        event['response']['failAuthentication'] = True
        event['response']['issueTokens']        = False
        return event

    session = event['request']['session']
    
    if(len(session)>0 and session[-1]['challengeResult']):
        event['response']['failAuthentication'] = False
        event['response']['issueTokens'] = True
        return event
    
    event['response']['failAuthentication'] = False
    event['response']['issueTokens'] = False

    
    
    return event