from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Have items show as actual name in admin area
    def __str__(self):
        return self.name

        
# class User(models.Model):
#     user_id = models.IntegerField()
#     username = models.CharField(max_length=15, null=False, blank=False)
#     password = 