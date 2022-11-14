# Basic discord bot 


import discord
# Don't use discord.ext as it is deprecated

# Fix SSL issues [https://stackoverflow.com/questions/59411362/ssl-certificate-verify-failed-certificate-verify-failed-unable-to-get-local-i]





client = discord.Client(
    intents=discord.Intents.default()
)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #create_role("Creating role", "interact", discord.Colour(0x00ff00))
    # Send a message to the channel
    #await message.channel.send('Hello!')


    # Join GUILD "893914383317622786"
    guild = client.get_guild(893914383317622786)
    # List members
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    

    # Make bot join guild

@client.event
async def on_message(message: discord.Message):
    print(message.guild)
    if message.author == client.user:
        return

    #if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


