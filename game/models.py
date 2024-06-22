from django.db import models

class Game(models.Model):

    nome = models.CharField(max_length=50)
    mini_descricao = models.TextField(max_length=400)
    imagem_destaque = models.ImageField(upload_to="fotos/", blank=True, null=True)
    imagem_miniatura = models.ImageField(upload_to="fotos/")
    descricao_completa = models.TextField(max_length=2000,  blank=True, null=True)
    imagem_gameplay1 = models.ImageField(upload_to="fotos/")
    imagem_gameplay2 = models.ImageField(upload_to="fotos/")
    imagem_gameplay3 = models.ImageField(upload_to="fotos/")
    imagem_gameplay4 = models.ImageField(upload_to="fotos/")
    imagem_solta = models.ImageField(upload_to="fotos/", blank=True, null=True)
    data_de_lancamento = models.CharField(max_length=50)
    desenvolvedor = models.CharField(max_length=50)
    estudio = models.CharField(max_length=50)

