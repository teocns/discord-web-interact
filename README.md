

# INTEGRATION PROCESS
1. Preparation


Have an applciation created at https://discordapp.com/developers/applications
    - Ensure to Enable the Server Members Intent for your application
    - Copy `CLIENT_ID` and `SECRET` into `config.py`
    - Important: Set the redirect URI of your OAuth2 application to the URL where your users will be redirected after they approve your application.
        For now, we are using `https://localhost:8080/authorize-discord`


Add a bot to your application

https://discordpy.readthedocs.io/en/stable/discord.html

Once completed, retrieve the secret token and and copy it into `config.py`
The token should look something like `ODkzOTEyMjg2MTc4MjAxNjQw.GeOC65.qW1jWMro1P88y5nmG_a62FLK0Odaj7DmiFFqA8`

2. Authorization

User links their Discord server
    - Request the user's permission to use Server Members Intent with the following scopes: `identify guilds`, `bot`
    - Request something like:
        https://discord.com/oauth2/authorize?response_type=code&client_id=893912286178201640&scope=identify%20bot&prompt=consent&state=15773059ghq9183habn&redirect_uri=https%3A%2F%2Flocalhost%3A8080%2Fauthorize-discord




On success, we will get a redirect to something like:
`https://localhost:8080/authorize-discord?code=VQQTk4JK0WGUsprJiZqcunUjNOYPRQ&state=15773059ghq9183habn&guild_id=893914383317622786&permissions=0`
`https://localhost:8080/authorize-discord?code=V0HJdjunARO0NYJRWkRG0CjrsHH75i&state=15773059ghq9183habn&guild_id=893914383317622786&permissions=0`

Our backend will parse the `code`, `guild` (which represents the server ID) and `state`



3. OAuth token generation

3.1 Use `code` received from the previous authorization process
3.2 Make a request to https://discordapp.com/api/oauth2/token with the following parameters:

    client_id: The client ID of your Discord application
    client_secret: The client secret of your Discord application
    grant_type: authorization_code
    code: The code retrieved from the redirect URL
    redirect_uri: The redirect URI of your Discord application

