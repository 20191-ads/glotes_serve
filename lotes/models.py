from django.db import models

# Create your models here.
class Lote(models.Model):

    mz = models.CharField(max_length=10)
    lt = models.CharField(max_length=10)
    direccion = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    class Meta:
        verbose_name = ("Lote")
        verbose_name_plural = ("Lotes")

    def __str__(self):
        return self.mz

    def get_absolute_url(self):
        return reverse("Lote_detail", kwargs={"pk": self.pk})
