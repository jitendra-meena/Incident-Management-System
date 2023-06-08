from datetime import datetime
from django.db import models
import random

class Incident(models.Model):
    INCIDENT_STATUS_CHOICES = (
        ('Open', 'Open'),
        ('In progress', 'In progress'),
        ('Closed', 'Closed'),
    )

    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    reporter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    incident_id = models.CharField(max_length=20, unique=True)
    incident_details = models.TextField()
    reported_datetime = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=INCIDENT_STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.incident_id:
            self.incident_id = f'RMG{random.randint(10000, 99999)}{datetime.now().year}'
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.incident_details