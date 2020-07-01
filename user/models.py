import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from django.utils.timezone import utc


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            print('user must need phone number')
            raise ValueError('Users must have an phone')

        user = self.model(
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_new_user(self, phone, username, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            print('user must have phone number')
            raise ValueError('Users must have an phone')

        user = self.model(
            phone=phone,
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, phone, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_ = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone=phone,
            password=password,

        )

        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(
        verbose_name='phone',
        max_length=20,
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=20,
        unique=True,
    )
    email = models.CharField(
        verbose_name='email',
        max_length=20,
        unique=True,
    )
    is_verify = models.BooleanField(
        verbose_name='is_verify',
        default=False
    )

    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'phone'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.username+"  "+self.phone


class Otp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    OTP = models.IntegerField(null=True)
    attempts = models.IntegerField(default=5)
    time_generate_otp = models.DateTimeField(auto_now_add=True, blank=True)

    def get_time_diff(self):
        if self.time_generate_otp:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.time_generate_otp
            return timediff.total_seconds()

    def __str__(self):
        return self.user.username