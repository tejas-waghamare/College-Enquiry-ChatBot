# from django.db import models

# class User_new(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     contact = models.CharField(max_length=15)


from django.db import models

class User_new(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name
