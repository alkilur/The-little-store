
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Email verification object for {self.user.username}"

    def send_verification_email(self):
        link = reverse('users:verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'

        subject = f'Подтверждение учетной записи {self.user.username}'
        message = f'Для подтверждения учетной записи {self.user.email} перейдите по ссылке: {verification_link}'

        send_mail(
                   subject=subject,
                   message=message,
                   from_email=settings.EMAIL_HOST_USER,
                   recipient_list=[self.user.email],
                   fail_silently=False,
                 )

    def is_expired(self):
        '''Метод проверки срока ссылки'''
        return now() >= self.expiration