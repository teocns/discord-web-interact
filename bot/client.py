import discord
from discord.ext import commands
from eventemitter import EventEmitter


class BotClient(commands.Bot):
    


    __event_emitter = EventEmitter()


    async def on_message(self, message: discord.Message):
        await self.__event_emitter.emit("message", message)

    async def on_ready(self):
        await self.__event_emitter.emit("ready")


    def on(self, event, listener):
        self.__event_emitter.add_listener(event, listener)
    

    def off(self, event, listener):
        self.__event_emitter.remove_listener(event, listener)