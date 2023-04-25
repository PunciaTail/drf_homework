from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# User를 생성할 때 사용하는 헬퍼 클래스
class UserManager(BaseUserManager):
    # 사용자를 생성
    def create_user(self, email, name, gender,  age, bio, password=None):
        if not email:
            raise ValueError("이메일을 입력하세요")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            bio=bio,
        )
        # 장고에서 제공하는 password 설정 함수
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 생성
    def create_superuser(self, email, name, gender, age, bio, password=None):
        user = self.create_user(
            email,
            name=name,
            gender=gender,
            age=age,
            bio=bio,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    GENDER_CHOICE = {
        ('male', 'Male'),
        ('female', 'Female'),
    }

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, blank=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    bio = models.TextField(blank=True)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 쉽게 말해 login ID
    USERNAME_FIELD = "email"

    # 이거 없으면 cratesuperuser 만들때 에러남
    REQUIRED_FIELDS = ["name", "gender", "age", "bio"]

    def __str__(self):
        return self.email
    
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

