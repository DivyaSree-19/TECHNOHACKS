# models.py
from django.db import models

class MyappList(models.Model):
    STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,null=True)

    class Meta:
        db_table = 'MyappList'




