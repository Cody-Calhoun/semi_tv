from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) <2:
            errors ['title'] = "Please enter at least 2 characters for the title"
        
        if len(post_data['network']) < 3:
            errors ['network'] = "Please enter 3 characters or more for the network"

        if len(post_data['description']) < 10:
            errors ['description'] = "Please enter 10 characters or more for the description"

        return errors

class Show (models.Model):
    title = models.CharField( max_length=255)
    network = models.CharField( max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = ShowManager()