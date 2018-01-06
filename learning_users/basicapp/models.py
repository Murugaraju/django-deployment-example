from django.db import models
from django.contrib.auth.models import User
"""
Built in User model attributes
username
email
paasword
firstname
surname/lastname
"""

# Creating model another model UserProfileInfo because we want to add addition attriute to default User model builtin function in django

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE )

    # here creating additional attribute to the model
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField( upload_to='profile_pics',blank=True)


    def ___str___ (self):
        return self.user.username
