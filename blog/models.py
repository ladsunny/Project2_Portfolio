from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    tags = models.CharField(max_length=300)

    def summary(self):
        return self.body[:250]

    def __str__(self):
        return self.title
