from django.urls import reverse
from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False, verbose_name="Descrição")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome

    def get_absolute_url(self):
        return reverse("loja_app:detail-produto", kwargs={"pk": self.pk})