from django.test import TestCase

from factory.django import DjangoModelFactory
from .models import DataFile


class DataFileFactory(DjangoModelFactory):
    file_name = 'test.json'
    file_type = 'json'
    date_loaded = '2019-06-26'

    class Meta:
        model = DataFile
        # django_get_or_create = ('created', 'updated')


class DataFileModelsTests(TestCase):
    def setUp(self):
        self.data_file = DataFileFactory.create()

    def test_get_file_name(self):
        self.assertEqual(self.data_file.file_name, 'test.json')
