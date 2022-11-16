from . import IConfigurationProvider
from services.firebase import FirebaseService

class FirebaseConfigProvider(IConfigurationProvider):
    def get_config(self) -> dict:
        return FirebaseService.discord_conf()