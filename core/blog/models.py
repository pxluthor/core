from ckeditor.fields import RichTextField
from django.db import models
#from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = RichTextField(blank=True, null=True)
    conteudo = RichTextUploadingField()
    imagem_capa = models.ImageField(null=True, blank=True, upload_to='core/static/blog/')
    data_publicacao = models.DateTimeField(timezone.now())

    def __str__(self) -> str:
        return self.titulo 