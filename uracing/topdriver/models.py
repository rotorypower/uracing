from django.db import models


class Driver(models.Model):
    CHOICES = (
        ('AWD', 'All Wheel Drive'),
        ('FWD', 'Front Wheel Drive'),
        ('RWD', 'Rear Wheel Drive'),
    )
    axle_drive = models.CharField(max_length=10, choices=CHOICES, default="FWD")
    driver_name = models.CharField(max_length=200)
    driver_car = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.axle_drive