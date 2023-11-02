from django.db import models


class Menu(models.Model):
    name = models.CharField(
        "Название",
        max_length=100,
        unique=True,
        blank=False,
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="heir",
        on_delete=models.CASCADE,
    )
    url = models.CharField(
        "Ссылка",
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
