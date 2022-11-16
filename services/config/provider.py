from .sources import IConfigurationProvider
from datetime import datetime
from .sources.enum import SOURCES


class ConfigurationProvider:
    """A persistent configuration provider"""
    _instance: IConfigurationProvider
    _cache: dict

    LAST_FETCH = None


    def __init__(
        self,
        source: SOURCES,
        *args,
    ) -> None:
        self._instance = source.value(*args)


        

    def get_config(self) -> dict:
        if self.cache_invalidated:
            self._cache = self._instance.get_config()
            self.LAST_FETCH = datetime.now()
        return self._cache

    

    @property
    def cache_invalidated(self):
        return not self.LAST_FETCH or (datetime.now() - self.LAST_FETCH).seconds > self._instance.CACHE_TTL

