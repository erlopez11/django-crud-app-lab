from django.db import models
from django.urls import reverse

PROGRESS_STATUS = (
    ('P', 'Planned'),
    ('IP', 'In-Progress'),
    ('C', 'Complete')
)

NEEDLE_SIZE = (
    ('00000', '1.0mm US 00000'),
    ('0000', '1.25mm US 0000'),
    ('000', '1.5mm US 000'),
    ('00', '1.75mm US 00'),
    ('0', '2mm US 0'),
    ('1', '2.25mm US 1'),
    ('1.5', '2.5mm US 1.5'),
    ('2', '2.75mm US 2'),
    ('2.5', '3mm US 2.5'),
    ('3', '3.25mm US 3'),
    ('4', '3.5mm US 4'),
    ('5', '3.75mm US 5'),
    ('6', '4.0mm US 6'),
    ('7', '4.5mm US 7'),
    ('8', '5mm US 8'),
    ('9', '5.5mm US 9'),
    ('10', '6mm US 10'),
    ('10.5', '6.5mm US 10.5'),
    ('11', '8mm US 11'),
    ('13', '9mm US 13'),
    ('14', '9.5mm US 14'),
    ('15', '10mm US 15'),
    ('17', '12mm US 17'),
    ('19', '16mm US 19'),
    ('35', '19mm US 35'),
    ('50', '25mm US 50'),
)

class Project(models.Model):

    name = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)
    progress_status = models.CharField(choices=PROGRESS_STATUS, default=PROGRESS_STATUS[0][0])
    needle_size = models.CharField(choices=NEEDLE_SIZE, default=NEEDLE_SIZE[13][0])
    cast_on = models.DateField(null=True, blank=True)
    cast_off = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'project_id': self.id})


class Note(models.Model):
    date = models.DateField('Knitting Session Date')
    notes = models.TextField()
    current_row = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'On {self.current_row} row on {self.date}'
    class Meta:
        ordering = ['-date']