from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from core.enums.action_token_enum import ActionTokenEnum
from core.exceptions.jwt_exception import JWTException

User = get_user_model()

ActionTokenClassType = Type[BlacklistMixin | Token]


class ActionToken(BlacklistMixin, Token):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime


class RecoveryToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY.token_type
    lifetime = ActionTokenEnum.RECOVERY.lifetime


class JWTService:
    @staticmethod
    def create_token(user: User, token_cls: ActionTokenClassType) -> Token:
        return token_cls.for_user(user)

    @staticmethod
    def verify_token(token: Token, token_cls: ActionTokenClassType) -> User:
        try:
            token_res = token_cls(token)
            token_res.check_blacklist()
        except Exception:
            raise JWTException

        token_res.blacklist()
        user_id = token_res.payload.get("user_id")
        return get_object_or_404(User, pk=user_id)
