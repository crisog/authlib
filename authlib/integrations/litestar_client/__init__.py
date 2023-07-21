# flake8: noqa

from ..base_client import BaseOAuth, OAuthError
from .integration import LitestarIntegration
from .apps import LitestarOAuth1App, LitestarOAuth2App


class OAuth(BaseOAuth):
    oauth1_client_cls = LitestarOAuth1App
    oauth2_client_cls = LitestarOAuth2App
    framework_integration_cls = LitestarIntegration

    def __init__(self, config=None, cache=None, fetch_token=None, update_token=None):
        super(OAuth, self).__init__(
            cache=cache, fetch_token=fetch_token, update_token=update_token
        )
        self.config = config


__all__ = [
    "OAuth",
    "OAuthError",
    "LitestarIntegration",
    "LitestarOAuth1App",
    "LitestarOAuth2App",
]
