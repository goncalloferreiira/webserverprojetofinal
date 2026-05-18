from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField()
    # Novos campos para links da internet (Internet Archive, etc.)
    url_poster = models.URLField(blank=True, null=True, help_text="Link da imagem do poster")
    url_video = models.URLField(blank=True, null=True, help_text="Link do filme no Internet Archive")

    def __str__(self):
        return self.titulo