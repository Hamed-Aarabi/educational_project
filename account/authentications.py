from django.contrib.auth.backends import BaseBackend
from .models import MyUser



class AuthWithEmail(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = MyUser.objects.get(id=user_id)
            return user
        except MyUser.DoesNotExist:
            return None


class AuthWithUsername(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(username=username)
            if user.check_password(password):
                return user
            return None
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = MyUser.objects.get(id=user_id)
            return user
        except MyUser.DoesNotExist:
            return None
