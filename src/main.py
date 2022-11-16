from bot import BOT

from services.config import Config



BOT_SECRET_TOKEN = Config.get("BOT_SECRET_TOKEN")


bot = BOT.launch(BOT_SECRET_TOKEN)
