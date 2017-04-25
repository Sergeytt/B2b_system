from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    create_at = models.DateField()
    auhtor = models.CharField(max_length=20)

    class Meta():
        verbose_name = "Блог"
        verbose_name_plural = "Блог"

    def __str__(self):
        return self.name


