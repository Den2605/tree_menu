from django.db import models


class Menu(models.Model):
    """Меню."""

    name = models.CharField(
        "Название",
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        "Идентификатор меню",
        max_length=255,
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/tree/{self.slug}/"


class Item(models.Model):
    """Пункты меню."""

    name = models.CharField(
        "Название",
        max_length=100,
        unique=True,
        blank=False,
    )
    slug = models.SlugField(
        "Идентификатор пункта",
        max_length=255,
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="childrens",
        on_delete=models.CASCADE,
    )
    menu = models.ForeignKey(
        Menu,
        blank=True,
        related_name="items",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/tree/{self.slug}/"
