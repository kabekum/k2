from django.db import models

class Client(models.Model):
    CLIENT_TYPE = [
        ('individual', 'Individual'),
        ('organization', 'Organization'),
    ]

    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
