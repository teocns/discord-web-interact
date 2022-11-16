
def env(key, default=None):
    """
    Get an environment variable or default to a value
    """
    import os
    return os.environ.get(key, default)



DEBUG = env('DEBUG', False)

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '893912286178201640'
CLIENT_SECRET = 'AJZ64HbhYyftSUIVHtMGoW4DiwP241dP'
REDIRECT_URI = 'https://localhost:8080/authorize-discord'


# Manage: SERVER, ROLES, CHANNELS
# Send: Messages
BOT_PERMISSIONS = 268437552
BOT_AUTHENTICATION_SCOPES = [
    'bot',
    'identify',
    'guilds',
    #'manage_roles',
    'guilds.join',
'guilds',
    'applications.commands'
]



FIREBASE_CERTIFICATE = {
  "type": "service_account",
  "project_id": "interact2002",
  "private_key_id": "31aa26f0d8a749a0654c59519905b33c65ba5a4b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDdLVoDQRFp0ut2\n22fluVvqpiBCbGl8qvzFyaLBf+RetGFb/ydPK3ECXbIjhdhg2Z0zE8ouqMpkuJIs\nDUvdriBLn/rjkD5DILcg0g8r3Q3qUf5QVhqFh5SL+eqcF2TSz3kSooEU2PH+V9L3\ntqHqZsXUH6Zah9r6t0z7xS7UE3qHTWLqDCU4tLgt3zzRGWfG0SMqLvk7P+6A4K/e\nIzJiV1RfsVLWXZ9lk5cW4i/65JIxC+yXVBv05BbUC8yPeB3ZxF2AkOaGanJ97tyV\nBV8wKtO08v1YQPh1aPCZNQcSfTV+YBumrFC+BEv7kjMM1xeZ/IG79Ikms/Waui7g\ndUQCh4EFAgMBAAECggEAFldqbEG6XJItrsfi6tWab01wnMUOssUi22fOxPUCQH7A\nBubzNZARzkdgoy31+XKB6pLpLWVnbF0ohsKhEzdvk7QJR8tePrGjTfFqDug5a530\nrnDEJRDY9Hq+NB441QKYHEXF/DEd4K9GZDdSi7bt7Mt1pldqy0CQyi3U2R9OlTQP\n4vUA8e8uowMlwYPgf1sYZMGnJz+Xr8IupkLQXLts0RZqYBOmq+K93WuSX1anBEoM\nS6EHZoQue55ryNGcZv9HBLJ7bDLIDuKxgAB4JSBtmH+ZjpwbIt9v9VFmFdP/hCsD\nA6QUj86NkFxf6BRe8IZRPVkCq2BUOpSo3wNLeTvOgQKBgQDvcYJ77L4Zn6zQGmb2\n8Mk7CEDIJsk8ZPSxhEpxQMjq6ZDO1qj9nLYo6aGmfpg1SxrSXanHqZ2R7U7v1z5I\ngMyEQ8kxaCv9us/mmFTUEcHptxo/qL8VVTjTWLO5oHrqNLU2WqrzjRRDGNsYoo0n\nDIiBalgvecvSn1WuXd7s/bQ7qQKBgQDseIDZIoDiOL46aoerpSq4V18dF0vjyY7v\no5LkG2CQ4r53rrpnVRuLj2uMAKrIcZRFKYbxx1jjQ/n8Jk5b5eWEoH4S6CyoXJ1S\nYhXa35YhfKPqJhWySRRRCp99Hhcf0MM2ZxwdxozUfXpNcWS82pda+dGPfXU4/Tbk\nSwy7FAMT/QKBgQCftyRlizYGm4bHTUUvJM/lq4yitZR3z5OUsXyCbMdYQrHP9knE\n2Xp8cdLc3waiTdW3SrjMMOylARktTHMEI73H3/tdFHJ7jdfNpgC3cJzbS8KbgfDr\nxuvftgQ0JsK2ZLAXcIUlbg587yB+HzduO6L2SDxIdsKpXJTneUAQ7u4A+QKBgQDa\nzv5a7SRZL6xGHYEAgMqw3Jf0MTRVyJHsiG1JiVOnfUhFMnblWsksMD+RwqRE6WQL\nQ0vMuWs0kBfnDAMB4g6o1GEUWaXI/DnOm1ghuTYQMmbyKN92o0ybWLsPaSJ4nBGm\na26G1sxFav4aXsyaO6JF2lfg8HPhkdyTDibvjKr0eQKBgGVFF01QrmdsB9VtU+R8\nMMENhfjlpPlymbfIyFk3FKJUeS+Ruf+4HqHLvCMFLONdNzXclcE4cdLoEnfgpdVa\nZhCLV8wHlNljGTr7afQOrtqjor0098LTTf65kr9ZjKzh5m3pKXV6IArUi01JulJY\nyQvr14WvHG9ta+SMQwIg6p1u\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-susel@interact2002.iam.gserviceaccount.com",
  "client_id": "110239609403364299926",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-susel%40interact2002.iam.gserviceaccount.com"
}




from utils.logging import setup


setup(DEBUG)