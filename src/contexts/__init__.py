# Define specific contexts for the bot to run in.



    



import abc

class IBotContext(abc.ABC):
    """An interface that represents a context for a bot."""

    @abc.abstractmethod
    async def on_message():
        pass

    @abc.abstractmethod
    async def on_ready():
        pass
