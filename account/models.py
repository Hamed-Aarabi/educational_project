from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager


class MyUser(AbstractBaseUser):
    CHOICE_SEX = (
        ('man', 'مرد'),
        ('woman', 'زن'),
        ('other', 'دیگر'),
    )
    email = models.EmailField(verbose_name="آدرس ایمیل", max_length=255, null=True)
    first_name = models.CharField(verbose_name='نام', max_length=255)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=255)
    username = models.CharField(verbose_name='نام کاربری', max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to='profiles', blank=True)
    phone = models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن')
    sex = models.CharField(choices=CHOICE_SEX, max_length=5, verbose_name='جنسیت')
    date_joined = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

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

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f'{self.email}{self.phone[-2:]}'
        # if self.is_teacher:
        #     Teacher.objects.create(teacher=self)
        return super(MyUser, self).save(*args, **kwargs)


class Ticket(models.Model):
    user = models.ForeignKey(MyUser, related_name='user_tickets', on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(verbose_name='متن تیکت')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'
