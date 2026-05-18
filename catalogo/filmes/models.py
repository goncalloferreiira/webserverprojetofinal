from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField()
    url_poster = models.URLField(blank=True, null=True)
    url_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    @property
    def media_notas(self):
        comentarios = self.comentarios.all()
        if comentarios:
            soma = sum(c.nota for c in comentarios)
            return round(soma / len(comentarios), 1)
        return "Sem notas"

class Comentario(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    nota = models.IntegerField(default=5)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} - {self.nota} Estrelas"