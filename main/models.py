from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        related_name='slider_images',
        verbose_name='Изображение'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['order']

    def __str__(self):
        return self.title