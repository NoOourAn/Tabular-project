from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None,cc=None,gender=None,age=None,univ=None,faculty=None,level=None ,is_S=False,is_U=True):
        if not email:
            raise ValueError("user must have an email address")
        if not username:
            raise ValueError("user must have username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            cc=cc,
            gender=gender,
            age=age,
            univ=univ,
            faculty=faculty,
            level=level,
            is_U=is_U,
            is_S = is_S


        )

        user.set_password(password)

        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False


        user.save(using=self.db)
        return user
    #
    # def create_Suser(self,username,email,password=None,cc='0',gender=None,age=None,univ=None,faculty=None,level=None ,):
    #     if not email:
    #         raise ValueError("user must have an email address")
    #     if not username:
    #         raise ValueError("user must have username")
    #
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         username=username,
    #         cc=cc,
    #         gender=gender,
    #         age=age,
    #         univ=univ,
    #         faculty= faculty,
    #         level=level,
    #
    #     )
    #
    #     user.set_password(password)
    #
    #     user.is_admin = False
    #     user.is_staff = False
    #     user.is_superuser = False
    #     user.is_U = False
    #     user.is_S = True
    #
    #     user.save(using=self.db)
    #     return user

    def create_Auser(self, username, email, password=None,cc=None,gender=None,age=None,univ=None,faculty=None,level=None ,):
        if not email:
            raise ValueError("user must have an email address")
        if not username:
            raise ValueError("user must have username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            cc=cc,
            gender=gender,
            age=age,
            univ=univ,
            faculty=faculty,
            level=level,


        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,username,email,password,cc="0",gender='Male',age='0',univ="x",faculty="x",level='0' ,):
        user = self.create_Auser(
            email=self.normalize_email(email),
            password=password,
            username=username,
            cc=cc,
            gender=gender,
            age=age,
            univ=univ,
            faculty=faculty,
            level=level,


        )


        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_U = False
        user.is_S =  False


        user.save(using=self.db)
        return user



class Account(AbstractBaseUser):
    email            = models.EmailField(verbose_name="email" , max_length=60 , unique=True ,  primary_key= True)
    username         = models.CharField(max_length=30 ,unique=True)
    date_joined      = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login       = models.DateTimeField(verbose_name='lst login', auto_now=True)
    cc               = models.PositiveSmallIntegerField(verbose_name='cc' )
    age              = models.PositiveSmallIntegerField(verbose_name='age' )
    univ             = models.CharField(verbose_name="univ" ,max_length=60 ,)
    faculty          = models.CharField(verbose_name="faculty" ,max_length=30 ,)
    gender           = models.CharField(verbose_name="gender" ,max_length=10 ,)
    level            = models.PositiveSmallIntegerField(verbose_name='level' )
    is_active        = models.BooleanField(default=True)
    is_admin         = models.BooleanField(default=False)
    is_staff         = models.BooleanField(default=False)
    is_superuser     = models.BooleanField(default=False)
    is_U             = models.BooleanField(default=False)
    is_S             = models.BooleanField(default=False)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
