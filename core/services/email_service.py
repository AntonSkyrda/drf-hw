import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

User = get_user_model()


class EmailService:
    @classmethod
    def __send_email(
        cls, to: tuple[str], template_name: str, context: dict, subject: str
    ) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            to=to,
            from_email=os.environ.get("EMAIL_HOST_USER"),
            subject=subject,
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register(cls, user: User):
        token = JWTService.create_token(user, ActivateToken)
        url = f"http://127.0.0.1:8000/auth/activate/{token}/"
        cls.__send_email(
            to=(user.email,),
            template_name="register.html",
            context={
                "first_name": user.profile.first_name,
                "last_name": user.profile.last_name,
                "url": url,
            },
            subject="Activate your account",
        )

    @classmethod
    def recovery_password(cls, user: User):
        token = JWTService.create_token(user, RecoveryToken)
        url = f"http://127.0.0.1:8000/auth/recovery/{token}/"
        cls.__send_email(
            to=(user.email,),
            template_name="recovery.html",
            context={"url": url},
            subject="Recovery your account",
        )
