



from urllib.parse import urlencode
import random





def gen_oauth_prompt_url(
    client_id,
    scopes: list[str],
    redirect_uri,
):
    # Makes the OAuth flow URL to which users grants permissions to their discord server
    return "https://discord.com/oauth2/authorize?" + urlencode({
            "client_id": client_id,
            "scope": " ".join(scopes),
            "state": str(random.randint(1111111,9999999)),
            "redirect_uri":redirect_uri,
            "prompt":"consent",
            "response_type":"code",
            'permissions': 268437536
        })