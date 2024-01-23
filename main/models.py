from django.db import models
from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    picture = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='картинка (превью)')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    picture = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='картинка (превью)')
    description = models.TextField(verbose_name='описание')
    link_to_video = models.CharField(max_length=250, **NULLABLE, verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson', verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
