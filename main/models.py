from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# class Photo(models.Model):
#     images = models.ImageField('Фотография', upload_to='upload')
