import os
from .provider import ConfigurationProvider
from .sources.enum import SOURCES

class Config(object):

    provider = ConfigurationProvider(SOURCES.FIREBASE)

    @classmethod
    def get(self, key: str, default: any = None) -> any:
        """Attempts to retrieve either from environment, else from config provider which pulls data remotely"""
        return self.env(key) or self.provider.get_config().get(key) or default

    @classmethod
    def env(self, key: str, default: any = None) -> any:
        return os.environ.get(key, default)