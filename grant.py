import requests

from config import API_ENDPOINT,CLIENT_ID,CLIENT_SECRET, BOT_AUTHENTICATION_SCOPES

import json




def get_authorization_code(
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
        'redirect_uri': 'https://localhost:8080/authorize-discord',
        'code':'V0HJdjunARO0NYJRWkRG0CjrsHH75i'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Create full URL
    r = requests.request("POST", API_ENDPOINT + '/oauth2/token', data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    #r = requests.post('%s' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))

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
            json.dumps(get_authorization_code())
        )
