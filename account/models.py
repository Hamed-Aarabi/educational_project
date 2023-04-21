from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager

CHOICE_SEX = (
    ('man', 'مرد'),
    ('woman', 'زن'),
    ('other', 'دیگر'),
)


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="آدرس ایمیل", max_length=255, unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=255)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=255)
    username = models.CharField(verbose_name='نام کاربری', max_length=255)
    image = models.ImageField(upload_to='profiles')
    phone = models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن')
    sex = models.CharField(choices=CHOICE_SEX, max_length=5, verbose_name='جنسیت')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
