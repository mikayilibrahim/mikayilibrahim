from django.db import models

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):
    user  = models.ForeignKey("auth.User", on_delete= models.CASCADE,verbose_name="İstifadəçi")
    title = models.CharField(max_length=50,verbose_name="Başlıq")
    content = RichTextField()
    create_date = models.TimeField(auto_now_add=True,verbose_name="Tarix")
    article_image = models.FileField(blank = True,null = True ,verbose_name = "Şəkil")

    def __str__(self):
        return str(self.title)



 