from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="newsimg")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


from datetime import date
gender_list=(("M","Male"),("F","Female"))

class personDetails(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=70, null=True, blank=True, unique=True)
	phonenumber=models.CharField(max_length=10, null=True, blank=True)
	password = models.CharField(max_length=50,null=True, blank=True)

	 

	def __str__(self):
		return '%s' %(self.name)