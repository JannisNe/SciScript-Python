import requests
from requests import adapters
import ssl
from urllib3 import poolmanager


class TLSAdapter(adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)


def get_session():
    session = requests.session()
    session.mount('https://', TLSAdapter())
    return session