from django.db import models

status_choices = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined'),
)

admin_choices = (
    ('Admin', 'Admin'),
    ('User', 'User'),
)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=status_choices, default='Pending')
    admin = models.CharField(max_length=50, choices=admin_choices, default='User')
    
    def __str__(self):
        return self.first_name