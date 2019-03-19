from django.db import models


class Nurse(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "Nurse {0.name}".format(self)


class Provider(models.Model):
    name = models.CharField(max_length=255)
    nurses = models.ManyToManyField(Nurse)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    date = models.CharField(max_length=12)
    start = models.IntegerField()
    end = models.IntegerField()
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return "{0.date} with {0.nurse}".format(self)
