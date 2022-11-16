
import abc


class IConfigurationProvider(abc.ABC):

    # How many seconds to wait before invalidating configuration and polling new one
    CACHE_TTL = 60
    
    @abc.abstractmethod
    def get_config() -> dict:
        pass    
