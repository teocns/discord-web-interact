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


    def run(self, token: str, *, reconnect: bool = True, **kwargs) -> None:
        # reconnect: bool = True,
        # log_handler: Optional[logging.Handler] = MISSING,
        # log_formatter: logging.Formatter = MISSING,
        # log_level: int = MISSING,
        # root_logger: bool = False,
        kwargs['reconnect'] = reconnect
        # Disable logging of the library
        kwargs['log_level'] = 100
        return super().run(token, **kwargs)