from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class AuthenticationBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=username)|Q(phone_number=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

from store.users.auth_backends import AuthenticationBackend

authentification = AuthenticationBackend()

authentification.authenticate(username="0552092560" , password="helloworld")
