from django.db import models
from django.contrib.auth.models import User

User_type = (
    (0, "Select"),
    (1, "Student"),
    (2, "Teacher"),
    (3, "Working"),
    (4, "Other")
)
Gender_type = (
    (0, "Select"),
    (1, "Male"),
    (2, "Female"),
    (3, "Transgender"),
    (4, "Other")
)


class Category(models.Model):
    Name = models.CharField(max_length=200, null=True)
    DESC = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    Createdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name


class SubCategory(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SubCategory = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    Createdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.SubCategory


class Quiz(models.Model):
    Quiz_name = models.CharField(max_length=50)
    Quiz_Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Quiz_SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    desc = models.CharField(max_length=500)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")

    def __str__(self):
        return self.Quiz_name


class QuesModel(models.Model):
    QuizCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    QuizSubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    Quiz_Name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Quiz_Name


class User(models.Model):
    UserName = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Phone = models.CharField(max_length=200, null=True)
    usertype = models.IntegerField(choices=User_type, default=0)
    Gender = models.IntegerField(choices=Gender_type, default=0)
    Password = models.CharField(max_length=128, verbose_name='password')
    profilePic = models.ImageField(upload_to='profile_pics', blank=True)
    Createdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.UserName

