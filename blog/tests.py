from django.test import TestCase

from .models import Category


class CategoryTest(TestCase):
    def test_category_str(self) -> None:
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")
