from django.db import models
from django.conf import settings

# Create your models here.


class Red(models.Model):
    intensity = models.IntegerField()

    def __str__(self):
        return str(self.intensity)


class Blue(models.Model):
    intensity = models.IntegerField()

    def __str__(self):
        return str(self.intensity)


class Green(models.Model):
    intensity = models.IntegerField()

    def __str__(self):
        return str(self.intensity)


class PixelCount(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return str(self.count)


class ColorCode(models.Model):
    code_red = models.ForeignKey(Red, on_delete=models.DO_NOTHING, null=True)
    code_green = models.ForeignKey(
        Green, on_delete=models.DO_NOTHING, null=True)
    code_blue = models.ForeignKey(Blue, on_delete=models.DO_NOTHING, null=True)
    pixels = models.ForeignKey(
        PixelCount, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        unique_together = (('code_red', 'code_blue', 'code_green', 'pixels'),)

    def __str__(self):
        return "R: %s, G: %s, B: %s" % (self.code_red, self.code_green, self.code_blue)


class SampleMeat(models.Model):
    mid = models.IntegerField(unique=True)
    color = models.ManyToManyField(ColorCode, blank=True)
    pixel_total = models.IntegerField(null=True)
    date_taken = models.DateTimeField()
    photo = models.FileField(upload_to='meat', null=True,
                             blank=True, max_length=500)

    class Meta:
        ordering = ['-date_taken']

    def __str__(self):
        return str(self.date_taken)
