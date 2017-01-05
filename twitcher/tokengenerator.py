"""
Provides various implementations of algorithms to generate an Access Token.
"""

import uuid

from twitcher.datatype import AccessToken, expires_at

import logging
logger = logging.getLogger(__name__)


def tokengenerator_factory(registry):
    return UuidTokenGenerator()


class TokenGenerator(object):
    """
    Base class for every token generator.
    """
    def create_access_token(self, valid_in_hours=1, environ=None):
        """
        Creates an access token.

        TODO: check valid in hours
        TODO: maybe specify how often a token can be used
        """
        token = AccessToken(
            token=self.generate(),
            expires_at=expires_at(hours=valid_in_hours),
            environ=environ)
        return token

    def generate(self):
        raise NotImplementedError


class UuidTokenGenerator(TokenGenerator):
    """
    Generate a token using uuid4.
    """
    def generate(self):
        """
        :return: A new token
        """
        return uuid.uuid4().get_hex()
