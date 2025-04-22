from django.db import models

class Project(models.Model):
    PROGRESS_STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in-progress', 'In-Progress'),
        ('complete', 'Complete')
    ]

    name = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)
    progress_status = models.CharField(choices=PROGRESS_STATUS_CHOICES, default='Planned')
    cast_on = models.DateField(null=True, blank=True)
    cast_off = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name