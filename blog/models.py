from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Excerpt(models.Model):
    class Meta:
        verbose_name_plural = "Excerpts"
        verbose_name = "Excerpt"
    excerpt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.excerpt
