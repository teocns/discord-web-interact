# Open a browser and navigate to the login page
# Use system default browser


import asyncio
from pyppeteer import launch
from pyppeteer.network_manager import Request
from oauth.factory import gen_oauth_prompt_url
from config import CLIENT_ID, BOT_AUTHENTICATION_SCOPES, REDIRECT_URI
from oauth.api import req_authorization_code



def on_auth_redirect(url):
    # Parse code, state, etc from the URL
    print('Redirected to %s' % url)

    # Parse URL parameters to dictionary
    params = dict(
        [part.split('=') for part in url.split('?')[1].split('&')]
    )

    token = req_authorization_code(
        code=params['code']
    )

    print(token)



async def on_request(browser, request: Request):
    if REDIRECT_URI in request.url:
        await on_auth_redirect(request.url)
    await request.continue_()
    #await getattr(sender,'continue')()


async def main():

    print('Launching browser')
    browser = await launch(
        headless=False,
    )
    page = await browser.newPage()
    oauth_url = gen_oauth_prompt_url(
        client_id=CLIENT_ID,
        scopes=BOT_AUTHENTICATION_SCOPES,
        redirect_uri=REDIRECT_URI
    )
    print('Navigating to %s' % oauth_url)

    # Go to the OAuth page
    #await page.setRequestInterception(True)

    # page.on('requestfinished', lambda *args: print({'requestfinished', args}))
    # page.on('requestfailed', lambda *args: print({'requestfailed', args}))
    # page.on('error', lambda *args: print({'error', args}))
    # page.on('pageerror',lambda *args: print({'pageerror', args}))
    # page.on('response', lambda *args: print({'response', args}))
    # page.on('requestservedfromcache', lambda *args: print({'requestservedfromcache', args}))
    # page.on('pageloadfailed', lambda *args: print({'pageloadfailed',args}))
    #await page.setRequestInterception(True)
    #page.on('request', lambda req: asyncio.ensure_future(on_request(browser,req)))
    

    # Just sleep infinitely without blocking the loop
    await page.goto(oauth_url)
    #await page.goto('https://localhost:8080/authorize-discord?code=BuJ3p1zfWj7pczrtd92lkVAxjlZDo5&state=1305584&guild_id=893914383317622786&permissions=0')
    while True:
        await asyncio.sleep(10)

asyncio.get_event_loop().run_until_complete(main())
