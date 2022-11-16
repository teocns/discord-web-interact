

from contexts import IBotContext
from bot.client import BotClient
import discord
import logging


log = logging.getLogger(__name__)
class BotContextsManager(object):
    
    client: BotClient

    def __init__(self, client) -> None:
        self.client = client

    contexts = {}
    
    def register(self, context):
        
        self.client.on("ready", context.on_ready)        
    

    def deregister(self, context):
        self.client.off("ready", context.on_ready)

    # def register_many(self, cls: IBotContext, *args):
    #     for arg in args:
            
    #         self.register(
    #             cls(arg)
    #         )


        