from django.db import models

# The model which is used in the entire application is been created here.
class article(models.Model):
	title = models.CharField(max_length = 200)
	auther = models.CharField(max_length = 200)
	publication_date = models.DateTimeField('date published')
	category = models.CharField(max_length = 100)
	hero_image = models.ImageField(upload_to = "images/")
	body = models.TextField()


