from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, phone, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an phone")

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            username=username,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            email=None,
            username=None,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user