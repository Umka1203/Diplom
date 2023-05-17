from django.db import models



class Link(models.Model):
    avtor = models.CharField('Автор', max_length=25)
    llink = models.CharField('Длинная ссылка', max_length=250)
    slink = models.CharField('Короткая ссылка', max_length=25)

    class Meta:

        constraints = [models.UniqueConstraint(fields=['avtor', 'slink'], name='unique_userlink')]
