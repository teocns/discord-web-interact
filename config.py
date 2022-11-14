DEBUG = True

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '893912286178201640'
CLIENT_SECRET = 'AJZ64HbhYyftSUIVHtMGoW4DiwP241dP'
REDIRECT_URI = 'https://localhost:8080/authorize-discord'


# Manage: SERVER, ROLES, CHANNELS
# Send: Messages
BOT_PERMISSIONS = 268437552
BOT_SECRET_TOKEN = 'ODkzOTEyMjg2MTc4MjAxNjQw.GeOC65.qW1jWMro1P88y5nmG_a62FLK0Odaj7DmiFFqA8'
BOT_AUTHENTICATION_SCOPES = [
    'bot',
    'identify',
    'guilds',
    #'manage_roles',
    'guilds.join',
'guilds',
    'applications.commands'
]
# The prefix for bot commands
BOT_COMMAND_PREFIX = '!'



# Voice channel created upon interaction schedule
INTERACT_CHANNEL_NAME = 'Interact-Winner'
INTERACT_CHANNEL_REQUIRED_ROLE = 'Interact-Winner'



if DEBUG:
    # Set logging to debug
    import logging
    logging.basicConfig(level=logging.DEBUG)