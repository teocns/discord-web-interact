import requests

from config import API_ENDPOINT,CLIENT_ID,CLIENT_SECRET, BOT_AUTHENTICATION_SCOPES,REDIRECT_URI

import json




def req_authorization_code(
    code,
):
    # client_id: The client ID of your Discord application
    # client_secret: The client secret of your Discord application
    # grant_type: authorization_code
    # code: The code retrieved from the redirect URL
    # redirect_uri: The redirect URI of your Discord application
    data = {
        'grant_type': 'authorization_code',
        'scope':' '.join(BOT_AUTHENTICATION_SCOPES),
        'redirect_uri': REDIRECT_URI,
        'code':code
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Create full URL

    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))

    try:
        r.raise_for_status()
    except:
        print(r.text)
        raise
    return r.json()

if __name__ == '__main__':
    # Write to tokens.json
    with open('tokens.json', 'w+') as f:
        f.write(
            json.dumps(req_authorization_code())
        )
